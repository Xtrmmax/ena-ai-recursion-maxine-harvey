import torch
import json
import os
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model
from datasets import Dataset

# ✅ Force GPU (Metal) on Apple Silicon
device = "mps" if torch.backends.mps.is_available() else "cpu"

# ✅ Ask user if they want to fine-tune an existing fine-tuned model or start fresh
use_existing_model = input("Do you want to fine-tune an existing fine-tuned model? (yes/no): ").strip().lower()

# ✅ Set the model path based on the choice
if use_existing_model == "yes":
    latest_model_path = max(
        [
            os.path.join("/Users/maxine-work/documents/github/AI-Engine/models/ollama-finetuned", d)
            for d in os.listdir("/Users/maxine-work/documents/github/AI-Engine/models/ollama-finetuned")
            if d.startswith("mistral-")
        ],
        key=os.path.getctime,
        default=None,
    )
    if latest_model_path:
        print(f"Using existing fine-tuned model: {latest_model_path}")
    else:
        print("No existing fine-tuned model found. Training from scratch.")
        latest_model_path = "/Users/maxine-work/documents/github/AI-Engine/models/mistral-7b"
else:
    latest_model_path = "/Users/maxine-work/documents/github/AI-Engine/models/mistral-7b"
    print("Training from scratch using base Mistral model.")

# ✅ Ensure structured storage for fine-tuned models
timestamp = datetime.now().strftime("%Y%m%d-%H%M")
output_dir = f"/Users/maxine-work/documents/github/AI-Engine/models/ollama-finetuned/mistral-{timestamp}"
os.makedirs(output_dir, exist_ok=True)

# ✅ Load dataset from JSON (1201 objects)
dataset_path = "/Users/maxine-work/documents/github/AI-Engine/mistral_base/data/vakog_dataset_clean.json"
with open(dataset_path, "r") as f:
    data = json.load(f)

# Convert to datasets.Dataset
dataset = Dataset.from_list(data)

# ✅ Verify dataset size and structure
print(f"Dataset size: {len(dataset)} objects")
for entry in dataset[:10]:  # Check first 10 for brevity
    if not all(key in entry for key in ["input", "output", "type"]):
        print(f"Warning: Missing keys in entry: {entry}")
        break

# ✅ Load model & tokenizer
tokenizer = AutoTokenizer.from_pretrained(latest_model_path)
tokenizer.pad_token = tokenizer.eos_token  # Fix: Set EOS token as PAD

model = AutoModelForCausalLM.from_pretrained(
    latest_model_path, 
    torch_dtype=torch.bfloat16,  # Use bfloat16 for MPS compatibility and efficiency
    device_map="auto"  # Automatically map to MPS for optimal device usage
)
model.to(device)  # Move model to GPU explicitly

# ✅ Apply LoRA for efficient fine-tuning
config = LoraConfig(
    r=16, 
    lora_alpha=32, 
    lora_dropout=0.05, 
    bias="none", 
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, config)

# ✅ Function to tokenize dataset (using 'input' and 'output')
def preprocess_function(examples):
    inputs = [f"User: {q} \nAssistant: {a}" for q, a in zip(examples["input"], examples["output"])]
    model_inputs = tokenizer(
        inputs, 
        padding="max_length",  # Force all sequences to be 512 tokens
        truncation=True, 
        max_length=512,  # Adjust based on data length if needed
        return_tensors="pt"
    )
    model_inputs["labels"] = model_inputs["input_ids"].clone()
    return model_inputs

# ✅ Tokenize the dataset
tokenized_dataset = dataset.map(
    preprocess_function,
    batched=True,  # Process in batches for efficiency
    remove_columns=dataset.column_names,  # Remove original columns after tokenization
    desc="Tokenizing dataset"
)

# ✅ Define training arguments (optimized for MacBook M4 Pro Max, without torch_compile)
training_args = TrainingArguments(
    output_dir=output_dir,  
    per_device_train_batch_size=8,  # Optimized for 40-core GPU and 128 GB RAM
    gradient_accumulation_steps=4,  # Balance performance and memory
    num_train_epochs=10,
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,  # Fewer logs for large datasets
    eval_strategy="no",
    save_total_limit=2,
    bf16=True,  # Use bfloat16 for MPS compatibility and efficiency
    remove_unused_columns=False,  
    push_to_hub=False,
    max_grad_norm=0.3,  # Prevent gradient explosion
    warmup_steps=100,  # Warm up for stable training
    learning_rate=2e-5,  # Conservative learning rate for stability
    optim="adamw_torch"  # Use native PyTorch AdamW for better MPS compatibility
)

# ✅ Start training
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset
)

trainer.train()

# ✅ Save fine-tuned model
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)

print(f"✅ Fine-tuning complete! Model saved in {output_dir}")
