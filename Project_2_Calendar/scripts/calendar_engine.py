import pandas as pd
from datetime import datetime, timedelta
import pytz
import json
import random
import numpy as np

# Global JSON data (loaded once at script start)
day_numbers, lords_of_day, birds, day_glyphs_json, lords_of_night, nahuals, directions, solar_wave_glyphs, year_glyphs = None, None, None, None, None, None, None, None, None

# Data for calculations
group_of_20 = [
    ("03-12", "03-31"), ("04-01", "04-20"), ("04-21", "05-10"), ("05-11", "05-30"),
    ("05-31", "06-19"), ("06-20", "07-09"), ("07-10", "07-29"), ("07-30", "08-18"),
    ("08-19", "09-07"), ("09-08", "09-27"), ("09-28", "10-17"), ("10-18", "11-06"),
    ("11-07", "11-26"), ("11-27", "12-16"), ("12-17", "01-05"), ("01-06", "01-25"),
    ("01-26", "02-14"), ("02-15", "03-06")
]

group_of_20_numbers = [
    [8, 2, 9, 3, 10, 4, 11, 5, 12, 6, 13, 7, 1],
    [2, 9, 3, 10, 4, 11, 5, 12, 6, 13, 7, 1, 8],
    [9, 3, 10, 4, 11, 5, 12, 6, 13, 7, 1, 8, 2],
    [3, 10, 4, 11, 5, 12, 6, 13, 7, 1, 8, 2, 9],
    [10, 4, 11, 5, 12, 6, 13, 7, 1, 8, 2, 9, 3],
    [4, 11, 5, 12, 6, 13, 7, 1, 8, 2, 9, 3, 10],
    [11, 5, 12, 6, 13, 7, 1, 8, 2, 9, 3, 10, 4],
    [5, 12, 6, 13, 7, 1, 8, 2, 9, 3, 10, 4, 11],
    [12, 6, 13, 7, 1, 8, 2, 9, 3, 10, 4, 11, 5],
    [6, 13, 7, 1, 8, 2, 9, 3, 10, 4, 11, 5, 12],
    [13, 7, 1, 8, 2, 9, 3, 10, 4, 11, 5, 12, 6],
    [7, 1, 8, 2, 9, 3, 10, 4, 11, 5, 12, 6, 13],
    [1, 8, 2, 9, 3, 10, 4, 11, 5, 12, 6, 13, 7],
    [8, 2, 9, 3, 10, 4, 11, 5, 12, 6, 13, 7, 1],
    [2, 9, 3, 10, 4, 11, 5, 12, 6, 13, 7, 1, 8],
    [9, 3, 10, 4, 11, 5, 12, 6, 13, 7, 1, 8, 2],
    [3, 10, 4, 11, 5, 12, 6, 13, 7, 1, 8, 2, 9],
    [10, 4, 11, 5, 12, 6, 13, 7, 1, 8, 2, 9, 3]
]

day_glyphs = ["Crocodile", "Wind", "House", "Lizard", "Snake",
              "Death", "Deer", "Rabbit", "Water", "Dog",
              "Monkey", "Healing Ivy", "Reed", "Jaguar", "Eagle",
              "Vulture", "Movement", "Flint", "Rain", "Flower"]

day_directions = ["East", "North", "West", "South",
                  "East", "North", "West", "South",
                  "East", "North", "West", "South",
                  "East", "North", "West", "South",
                  "East", "North", "West", "South"]

lord_night_table = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2],
    [3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4],
    [5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8],
    [9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3],
    [4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2],
    [3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4],
    [5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8],
    [9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3],
    [4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
]

lord_night_nahual_map = {
    1: ("Xiuhtecuhtli", "Scorpion"),
    2: ("Tezcatlipoca", "Bat"),
    3: ("Piltzintecuhtli", "Coyote"),
    4: ("Centeotl", "Spider"),
    5: ("Mictlantecuhtli", "Owl"),
    6: ("Chalchiuhtlicue", "Snake"),
    7: ("Tlazohteotl", "Obsidian Butterfly"),
    8: ("Tepeyolohtli", "Jaguar"),
    9: ("Tlaloc", "Water Serpent")
}

reference_table = pd.DataFrame({
    "52-Year Cycle Number": list(range(1, 53)),
    "Mexica Year Number": [(i % 13) + 1 for i in range(52)],
    "Mexica Year Name": ["Rabbit", "Reed", "Flint", "House"] * 13,
    "Anchor Years": [
        [1662, 1714, 1766, 1818, 1870, 1922, 1974, 2026],
        [1663, 1715, 1767, 1819, 1871, 1923, 1975, 2027],
        [1664, 1716, 1768, 1820, 1872, 1924, 1976, 2028],
        [1665, 1717, 1769, 1821, 1873, 1925, 1977, 2029],
        [1666, 1718, 1770, 1822, 1874, 1926, 1978, 2030],
        [1667, 1719, 1771, 1823, 1875, 1927, 1979, 2031],
        [1668, 1720, 1772, 1824, 1876, 1928, 1980, 2032],
        [1669, 1721, 1773, 1825, 1877, 1929, 1981, 2033],
        [1670, 1722, 1774, 1826, 1878, 1930, 1982, 2034],
        [1671, 1723, 1775, 1827, 1879, 1931, 1983, 2035],
        [1672, 1724, 1776, 1828, 1880, 1932, 1984, 2036],
        [1673, 1725, 1777, 1829, 1881, 1933, 1985, 2037],
        [1674, 1726, 1778, 1830, 1882, 1934, 1986, 2038],
        [1675, 1727, 1779, 1831, 1883, 1935, 1987, 2039],
        [1676, 1728, 1780, 1832, 1884, 1936, 1988, 2040],
        [1677, 1729, 1781, 1833, 1885, 1937, 1989, 2041],
        [1678, 1730, 1782, 1834, 1886, 1938, 1990, 2042],
        [1679, 1731, 1783, 1835, 1887, 1939, 1991, 2043],
        [1680, 1732, 1784, 1836, 1888, 1940, 1992, 2044],
        [1681, 1733, 1785, 1837, 1889, 1941, 1993, 2045],
        [1682, 1734, 1786, 1838, 1890, 1942, 1994, 2046],
        [1683, 1735, 1787, 1839, 1891, 1943, 1995, 2047],
        [1684, 1736, 1788, 1840, 1892, 1944, 1996, 2048],
        [1685, 1737, 1789, 1841, 1893, 1945, 1997, 2049],
        [1686, 1738, 1790, 1842, 1894, 1946, 1998, 2050],
        [1687, 1739, 1791, 1843, 1895, 1947, 1999, 2051],
        [1688, 1740, 1792, 1844, 1896, 1948, 2000, 2052],
        [1689, 1741, 1793, 1845, 1897, 1949, 2001, 2053],
        [1690, 1742, 1794, 1846, 1898, 1950, 2002, 2054],
        [1691, 1743, 1795, 1847, 1899, 1951, 2003, 2055],
        [1692, 1744, 1796, 1848, 1900, 1952, 2004, 2056],
        [1693, 1745, 1797, 1849, 1901, 1953, 2005, 2057],
        [1694, 1746, 1798, 1850, 1902, 1954, 2006, 2058],
        [1695, 1747, 1799, 1851, 1903, 1955, 2007, 2059],
        [1696, 1748, 1800, 1852, 1904, 1956, 2008, 2060],
        [1697, 1749, 1801, 1853, 1905, 1957, 2009, 2061],
        [1698, 1750, 1802, 1854, 1906, 1958, 2010, 2062],
        [1699, 1751, 1803, 1855, 1907, 1959, 2011, 2063],
        [1700, 1752, 1804, 1856, 1908, 1960, 2012, 2064],
        [1701, 1753, 1805, 1857, 1909, 1961, 2013, 2065],
        [1702, 1754, 1806, 1858, 1910, 1962, 2014, 2066],
        [1703, 1755, 1807, 1859, 1911, 1963, 2015, 2067],
        [1704, 1756, 1808, 1860, 1912, 1964, 2016, 2068],
        [1705, 1757, 1809, 1861, 1913, 1965, 2017, 2069],
        [1706, 1758, 1810, 1862, 1914, 1966, 2018, 2070],
        [1707, 1759, 1811, 1863, 1915, 1967, 2019, 2071],
        [1708, 1760, 1812, 1864, 1916, 1968, 2020, 2072],
        [1709, 1761, 1813, 1865, 1917, 1969, 2021, 2073],
        [1710, 1762, 1814, 1866, 1918, 1970, 2022, 2074],
        [1711, 1763, 1815, 1867, 1919, 1971, 2023, 2075],
        [1712, 1764, 1816, 1868, 1920, 1972, 2024, 2076],
        [1713, 1765, 1817, 1869, 1921, 1973, 2025, 2077]
    ],
    "Cipactli Number": [1, 10, 6, 2, 11, 7, 3, 12, 8, 4, 13, 9, 5] * 4,
    "Nemontemi Start Number": [1, 6, 11, 3, 8, 13, 5, 10, 2, 7, 12, 4, 9] * 4,
    "Nemontemi Start Glyph": ["Crocodile", "Death", "Monkey", "Vulture"] * 13
})

mexica_year_starts = {
    "Rabbit": ("03-12", "07:43:00"),
    "Reed": ("03-12", "13:43:00"),
    "Flint": ("03-11", "19:43:00"),
    "House": ("03-12", "01:43:00")
}

tz_dict = {
    "est": "America/New_York",
    "edt": "America/New_York",
    "cst": "America/Chicago",
    "cdt": "America/Chicago",
    "mst": "America/Denver",
    "mdt": "America/Denver",
    "pst": "America/Los_Angeles",
    "pdt": "America/Los_Angeles",
    "akst": "America/Anchorage",
    "akdt": "America/Anchorage",
    "hst": "Pacific/Honolulu",
    "nst": "America/St_Johns",
    "nfld": "America/St_Johns",
    "ast_ca": "America/Halifax",
    "adt_ca": "America/Halifax",
    "gmt": "Europe/London",
    "bst": "Europe/London",
    "cet": "Europe/Paris",
    "cest": "Europe/Paris",
    "eet": "Europe/Helsinki",
    "eest": "Europe/Helsinki",
    "msk": "Europe/Moscow",
    "msd": "Europe/Moscow",
    "wat": "Africa/Lagos",
    "cat": "Africa/Harare",
    "eat": "Africa/Nairobi",
    "sast": "Africa/Johannesburg",
    "ist": "Asia/Kolkata",
    "jst": "Asia/Tokyo",
    "cst_cn": "Asia/Shanghai",
    "kst": "Asia/Seoul",
    "sgt": "Asia/Singapore",
    "pht": "Asia/Manila",
    "gst": "Asia/Dubai",
    "irst": "Asia/Tehran",
    "irdt": "Asia/Tehran",
    "aest": "Australia/Sydney",
    "aedt": "Australia/Sydney",
    "acst": "Australia/Adelaide",
    "acdt": "Australia/Adelaide",
    "awst": "Australia/Perth",
    "brst": "America/Sao_Paulo",
    "brt": "America/Sao_Paulo",
    "art": "America/Argentina/Buenos_Aires",
    "clt": "America/Santiago",
    "gft": "America/Fortaleza",
    "myt": "Asia/Kuala_Lumpur",
    "idt": "Asia/Jerusalem",
    "wast": "Africa/Windhoek",
    "trt": "Europe/Istanbul",
    "uzt": "Asia/Tashkent",
    "pkt": "Asia/Karachi",
    "nzst": "Pacific/Auckland"
}

WEIGHTS = {
    "lord_of_night": 0.20,
    "nahual": 0.30,
    "day_glyph": 0.20,
    "day_number": 0.10,
    "lord_of_day": 0.05,
    "bird": 0.05,
    "solar_wave": 0.05,
    "year_glyph": 0.025,
    "year_number": 0.025
}

# Initialize JSON data
def load_json_files():
    global day_numbers, lords_of_day, birds, day_glyphs_json, lords_of_night, nahuals, directions, solar_wave_glyphs, year_glyphs
    base_path = "/Users/maxine-work/Documents/GitHub/AI-Engine/data/input/perselfie_calendar_input/"
    json_files = {
        "day_numbers": "simplified_day_number_foundation.json",
        "lords_of_day": "simplified_lord_of_day.json",
        "birds": "simplified_bird.json",
        "day_glyphs": "simplified_day_glyphs.json",
        "lords_of_night": "simplified_lord_of_night.json",
        "nahuals": "simplified_nahual.json",
        "directions": "simplified_direction.json",
        "solar_wave_glyphs": "simplified_solar_wave_glyphs.json",
        "year_glyphs": "simplified_year_glyphs.json"
    }
    for key, file_name in json_files.items():
        file_path = f"{base_path}{file_name}"
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                print(f"Successfully loaded {file_path}")
                if key == "day_numbers":
                    day_numbers = data["day_numbers"]
                elif key == "lords_of_day":
                    lords_of_day = data["lords_of_day"]
                elif key == "birds":
                    birds = data["birds"]
                elif key == "day_glyphs":
                    day_glyphs_json = data["day_glyphs"]
                elif key == "lords_of_night":
                    lords_of_night = data["lords_of_the_night"]
                elif key == "nahuals":
                    nahuals = data["nahuals"]
                elif key == "directions":
                    directions = data["directions"]
                elif key == "solar_wave_glyphs":
                    solar_wave_glyphs = data["solar_wave_glyphs"]
                elif key == "year_glyphs":
                    year_glyphs = data["year_glyphs"]
        except FileNotFoundError:
            print(f"Error: Could not find {file_path}")
            return None, None, None, None, None, None, None, None, None
        except json.JSONDecodeError:
            print(f"Error: {file_path} is corrupted or not valid JSON")
            return None, None, None, None, None, None, None, None, None
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return None, None, None, None, None, None, None, None, None
    return day_numbers, lords_of_day, birds, day_glyphs_json, lords_of_night, nahuals, directions, solar_wave_glyphs, year_glyphs

# Load JSON data globally
day_numbers, lords_of_day, birds, day_glyphs_json, lords_of_night, nahuals, directions, solar_wave_glyphs, year_glyphs = load_json_files()

def convert_numpy_types(obj):
    if isinstance(obj, np.int64):
        return int(obj)
    elif isinstance(obj, dict):
        return {k: convert_numpy_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(item) for item in obj]
    return obj

def get_mexica_year(year, month, day, hour=0, minute=0):
    naive_dt = datetime(year, month, day, hour, minute)
    est_tz = pytz.timezone("America/New_York")
    birth_date = est_tz.localize(naive_dt, is_dst=False)
    
    row_number = None
    for idx, years in enumerate(reference_table["Anchor Years"]):
        if year in years:
            row_number = idx + 1
            break
    if row_number is None:
        raise ValueError(f"Year {year} not found in the anchor years.")
    
    row_data = reference_table.iloc[row_number - 1]
    mexica_year_name = row_data["Mexica Year Name"]
    start_date_str, start_time_str = mexica_year_starts[mexica_year_name]
    start_hour, start_minute, start_second = map(int, start_time_str.split(":"))
    year_start_day = 11 if mexica_year_name == "Flint" else 12
    year_start_time = est_tz.localize(datetime(year, 3, year_start_day, start_hour, start_minute, start_second), is_dst=False)
    
    # Previous year end time
    prev_year = year - 1
    prev_row_index = (row_number - 2) % len(reference_table)
    prev_row_data = reference_table.iloc[prev_row_index]
    prev_mexica_year_name = prev_row_data["Mexica Year Name"]
    prev_start_date_str, prev_start_time_str = mexica_year_starts[prev_mexica_year_name]
    prev_start_hour, prev_start_minute, prev_start_second = map(int, prev_start_time_str.split(":"))
    prev_year_end_day = 6 if prev_mexica_year_name == "Flint" else 7
    prev_year_end_time = est_tz.localize(datetime(year, 3, prev_year_end_day, prev_start_hour, prev_start_minute, prev_start_second), is_dst=False)
    
    adjusted_year = year
    is_nemontemi = False
    
    if birth_date > prev_year_end_time and birth_date < year_start_time:
        is_nemontemi = True
        adjusted_year = prev_year
    
    if not is_nemontemi and birth_date < year_start_time:
        adjusted_year = prev_year
    
    row_number = None
    for idx, years in enumerate(reference_table["Anchor Years"]):
        if adjusted_year in years:
            row_number = idx + 1
            break
    if row_number is None:
        raise ValueError(f"Year {adjusted_year} not found in the anchor years.")
    
    row_data = reference_table.iloc[row_number - 1]
    result = {
        "Gregorian Year": year,
        "Adjusted Mexica Year": adjusted_year,
        "52-Year Cycle Number": row_data["52-Year Cycle Number"],
        "Mexica Year Number": row_data["Mexica Year Number"],
        "Mexica Year Name": row_data["Mexica Year Name"],
        "Cipactli Number": row_data["Cipactli Number"],
        "Nemontemi Start Number": row_data["Nemontemi Start Number"],
        "Nemontemi Start Glyph": row_data["Nemontemi Start Glyph"]
    }
    
    if is_nemontemi:
        nem_start_time = prev_year_end_time  # Nemontemi starts at previous year's end time
        elapsed = birth_date - nem_start_time
        # Calculate days with time precision
        days_to_roll = int(elapsed.total_seconds() // (24 * 3600))  # Floor division to get whole days
        if elapsed.total_seconds() % (24 * 3600) < 0:  # Handle negative time difference
            days_to_roll -= 1
        start_number = row_data["Nemontemi Start Number"]
        start_index = day_glyphs.index(row_data["Nemontemi Start Glyph"])
        nemontemi_day_number = (start_number + days_to_roll) % 13 or 13
        nemontemi_day_glyph_index = (start_index + days_to_roll) % 20
        nemontemi_day_glyph = day_glyphs[nemontemi_day_glyph_index]
        result["Nemontemi Day Number"] = nemontemi_day_number
        result["Nemontemi Day Glyph"] = nemontemi_day_glyph
    
    return result

def get_mexica_glyph(year, month, day, hour=0, minute=0, time_known=True):
    naive_dt = datetime(year, month, day, hour, minute)
    est_tz = pytz.timezone("America/New_York")
    birth_date = est_tz.localize(naive_dt, is_dst=False)
    
    birth_str = birth_date.strftime("%m-%d")
    year_result = get_mexica_year(year, month, day, hour, minute)
    mexica_year = year_result["Mexica Year Name"]
    adjusted_year = year_result["Adjusted Mexica Year"]
    if "Nemontemi Day Glyph" in year_result:
        return year_result["Nemontemi Day Glyph"], None
    
    start_date_str, start_time_str = mexica_year_starts[mexica_year]
    start_hour, start_minute, start_second = map(int, start_time_str.split(":"))
    
    # Calculate year_end_time for special case
    year_end_day = 6 if mexica_year == "Flint" else 7
    year_end_time = est_tz.localize(datetime(adjusted_year +1, 3, year_end_day, start_hour, start_minute, start_second), is_dst=False)
    
    year_start_day = 11 if mexica_year == "Flint" else 12
    year_start_time = est_tz.localize(datetime(adjusted_year, 3, year_start_day, start_hour, start_minute, start_second), is_dst=False)
    
    if month == 3 and day == year_start_day and birth_date >= year_start_time:
        group_position = 0
        mexica_day = 0
        glyph_index = mexica_day % 20
        result = day_glyphs[glyph_index]
        return result, group_position
    
    group_position = None
    group_start = None
    for idx, (start, end) in enumerate(group_of_20):
        start_month, start_day = map(int, start.split("-"))
        end_month, end_day = map(int, end.split("-"))
        start_year = year if not (start_month == 12 and birth_str < "01-06") else year - 1
        end_year = start_year + 1 if end_month < start_month else start_year
        start_date = datetime(start_year, start_month, start_day)
        end_date = datetime(end_year, end_month, end_day)
        if birth_date.date() >= start_date.date() and birth_date.date() <= end_date.date():
            group_position = idx
            group_start = start_date
            break
    
    if group_position is None and mexica_year != "Flint" and month == 3 and day == 7 and birth_date < year_end_time:
        group_position = 17
        group_start = datetime(year, 2, 15) if month == 3 and day == 7 else None  # adjust for the year
    
    if group_start is None:
        return "Date not in any Group of 20", None
    
    days_diff = (birth_date.date() - group_start.date()).days
    group_year = group_start.year
    is_leap = (group_year % 4 == 0 and (group_year % 100 != 0 or group_year % 400 == 0))
    leap_date = datetime(group_year, 2, 29).date() if is_leap else None
    if leap_date and group_start.date() < leap_date < birth_date.date():
        days_diff -=1
    
    mexica_day = days_diff
    if time_known and mexica_year != "Flint" and birth_date.time() < datetime(1900, 1, 1, start_hour, start_minute, start_second).time():
        mexica_day -= 1
    
    glyph_index = mexica_day % 20
    result = day_glyphs[glyph_index]
    if not time_known:
        result += " (Without your time of birth, this may not be accurate)"
    return result, group_position

def get_day_number(cipactli_number, group_position, glyph):
    glyph = glyph.split(" (")[0]
    first_row = group_of_20_numbers[0]
    column_index = first_row.index(cipactli_number)
    row = group_of_20_numbers[group_position]
    starting_number = row[column_index]
    glyph_index = day_glyphs.index(glyph)
    current_number = starting_number
    for i in range(glyph_index):
        current_number = (current_number % 13) + 1 if current_number < 13 else 1
    return current_number

def get_mexica_date(year, month, day, hour=0, minute=0, time_known=True):
    year_result = get_mexica_year(year, month, day, hour, minute)
    glyph, group_position = get_mexica_glyph(year, month, day, hour, minute, time_known)
    
    if "Nemontemi Day Number" in year_result:  # Nemontemi days
        day_number = year_result["Nemontemi Day Number"]
    else:  # Regular days
        cipactli_number = year_result["Cipactli Number"]
        day_number = get_day_number(cipactli_number, group_position, glyph)

    result = year_result
    result["Day Glyph"] = glyph
    result["Day Number"] = day_number
    result["Group Position"] = group_position
    return result

def get_lord_night_nahual(group_position, day_glyph):
    if group_position is None:
        return None, None, None
    glyph_index = day_glyphs.index(day_glyph)
    lord_number = lord_night_table[group_position][glyph_index]
    if lord_number not in lord_night_nahual_map:
        raise ValueError("Invalid lord of night number obtained.")
    lord, nahual = lord_night_nahual_map[lord_number]
    return lord_number, lord, nahual

def get_solar_wave(day_number, day_glyph):
    try:
        current_index = day_glyphs.index(day_glyph)
    except ValueError:
        raise ValueError("The provided day glyph is not in the known list.")
    solar_index = (current_index - (day_number - 1)) % 20
    solar_wave = day_glyphs[solar_index]
    solar_direction = day_directions[solar_index]
    return solar_wave, solar_direction

day_ruler_bird = {
    1: ("Xiuhtecuhtli", "Blue Hummingbird"),
    2: ("Tlaltecuhtli", "Green Hummingbird"),
    3: ("Chalchiuhtlicue", "Falcon"),
    4: ("Tonatiuh", "Quail"),
    5: ("Tlazohteotl", "Eagle"),
    6: ("Teoyaomicqui", "Small Owl"),
    7: ("Centeotl", "Obsidian Butterfly"),
    8: ("Tlaloc", "Obsidian Eagle"),
    9: ("Quetzalcoatl", "Turkey"),
    10: ("Tezcatlipoca", "Power Eagle"),
    11: ("Mictlantecuhtli", "Macaw"),
    12: ("Tlahuizcalpantecuhtli", "Quetzal"),
    13: ("Ilamatecuhtli", "Parrot")
}

def get_day_ruler_bird(day_number):
    if day_number < 1 or day_number > 13:
        raise ValueError("Day number must be between 1 and 13")
    return day_ruler_bird[day_number]

def generate_training_data(num_entries=10000):
    start_year = 1950
    end_year = 2025
    timezone = "America/New_York"
    est_tz = pytz.timezone(timezone)
    
    output_file = open("AI-Engine/data/output/perselfie_calendar_output/training_profiles.jsonl", "w", encoding='utf-8')
    
    if not all([day_numbers, lords_of_day, birds, day_glyphs_json, lords_of_night, nahuals, directions, solar_wave_glyphs, year_glyphs]):
        print("Failed to load JSON files. Exiting.")
        output_file.close()
        return
    
    entries_generated = 0
    
    while entries_generated < num_entries:
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Safe range to avoid invalid dates
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        
        naive_dt = datetime(year, month, day, hour, minute, 0)
        try:
            birth_date = est_tz.localize(naive_dt, is_dst=None)
        except pytz.exceptions.AmbiguousTimeError:
            birth_date = est_tz.localize(naive_dt, is_dst=False)
        except pytz.exceptions.NonExistentTimeError:
            naive_dt += timedelta(hours=1)
            birth_date = est_tz.localize(naive_dt, is_dst=True)
        
        try:
            entry = generate_dataset_entry(birth_date, day_numbers, lords_of_day, birds, day_glyphs_json, lords_of_night, nahuals, directions, solar_wave_glyphs, year_glyphs)
            output_file.write(json.dumps(convert_numpy_types(entry), ensure_ascii=False) + "\n")
            entries_generated += 1
            print(f"Generated {entries_generated}/{num_entries} entries")
        except Exception as e:
            est_time_str = birth_date.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Skipping date {est_time_str} due to error: {str(e)}")
            continue
    
    output_file.close()
    print(f"Generated {entries_generated} profiles in training_profiles.jsonl")

def generate_dataset_entry(birth_date, day_numbers, lords_of_day, birds, day_glyphs_json, lords_of_night, nahuals, directions, solar_wave_glyphs, year_glyphs):
    result = get_mexica_date(birth_date.year, birth_date.month, birth_date.day, 
                             birth_date.hour, birth_date.minute, True)
    is_nemontemi = "Nemontemi Day Number" in result
    
    if is_nemontemi:
        solar_wave, solar_direction = None, None
        ruler, bird = None, None
        lord_num, lord, nahual = None, None, None
    else:
        try:
            solar_wave, solar_direction = get_solar_wave(result["Day Number"], result["Day Glyph"])
            ruler, bird = get_day_ruler_bird(result["Day Number"])
            lord_num, lord, nahual = get_lord_night_nahual(result["Group Position"], result["Day Glyph"])
        except Exception as e:
            raise ValueError(f"Error processing non-Nemontemi elements: {str(e)}")
    
    elements = {
        "year_number": result["Mexica Year Number"],
        "year_name": result["Mexica Year Name"],
        "is_nemontemi": is_nemontemi
    }
    if is_nemontemi:
        elements["nemontemi_day_number"] = result["Nemontemi Day Number"]
        elements["nemontemi_day_glyph"] = result["Nemontemi Day Glyph"]
        elements["nemontemi_start_number"] = result["Nemontemi Start Number"]
        elements["nemontemi_start_glyph"] = result["Nemontemi Start Glyph"]
    else:
        elements["day_glyph"] = result["Day Glyph"]
        elements["day_number"] = result["Day Number"]
        elements["solar_wave"] = solar_wave
        elements["solar_direction"] = solar_direction
        elements["lord_of_day"] = ruler
        elements["bird"] = bird
        elements["lord_night_number"] = lord_num
        elements["lord_of_night"] = lord
        elements["nahual"] = nahual
    
    day_glyph_data = next((g for g in day_glyphs_json if g["day_glyph"] == elements.get("day_glyph", elements.get("nemontemi_day_glyph", ""))), None)
    day_glyph_traits = {
        "core_energy": day_glyph_data.get("core_energy", []) if day_glyph_data else [],
        "strengths": day_glyph_data.get("strengths", []) if day_glyph_data else [],
        "challenges": day_glyph_data.get("challenges", []) if day_glyph_data else []
    }
    
    if is_nemontemi:
        nemontemi_number_data = day_numbers.get(str(result["Nemontemi Day Number"]), {})
        day_number_traits = {
            "core_energy": nemontemi_number_data.get("core_energy", []),
            "strengths": nemontemi_number_data.get("strengths", []),
            "challenges": nemontemi_number_data.get("challenges", [])
        }
    else:
        day_number_data = day_numbers.get(str(elements["day_number"]), {})
        day_number_traits = {
            "core_energy": day_number_data.get("core_energy", []),
            "strengths": day_number_data.get("strengths", []),
            "challenges": day_number_data.get("challenges", [])
        }
    
    lord_of_night_traits = {"core_energy": [], "strengths": [], "challenges": []}
    if elements.get("lord_of_night"):
        lord_of_night_data = next((l for l in lords_of_night if l["name"] == elements["lord_of_night"]), None)
        lord_of_night_traits = {
            "core_energy": lord_of_night_data.get("core_energy", []) if lord_of_night_data else [],
            "strengths": lord_of_night_data.get("strengths", []) if lord_of_night_data else [],
            "challenges": lord_of_night_data.get("challenges", []) if lord_of_night_data else []
        }
    
    nahual_traits = {"core_energy": [], "strengths": [], "challenges": []}
    if elements.get("nahual"):
        nahual_data = next((n for n in nahuals if n["name"] == elements["nahual"]), None)
        nahual_traits = {
            "core_energy": nahual_data.get("core_energy", []) if nahual_data else [],
            "strengths": nahual_data.get("strengths", []) if nahual_data else [],
            "challenges": nahual_data.get("challenges", []) if nahual_data else []
        }
    
    lord_of_day_traits = {"core_energy": [], "strengths": [], "challenges": []}
    if elements.get("lord_of_day"):
        lord_of_day_data = next((l for l in lords_of_day if l["name"] == elements["lord_of_day"]), None)
        lord_of_day_traits = {
            "core_energy": lord_of_day_data.get("core_energy", []) if lord_of_day_data else [],
            "strengths": lord_of_day_data.get("strengths", []) if lord_of_day_data else [],
            "challenges": lord_of_day_data.get("challenges", []) if lord_of_day_data else []
        }
    
    bird_traits = {"core_energy": [], "strengths": [], "challenges": []}
    if elements.get("bird"):
        bird_data = next((b for b in birds if b["name"] == elements["bird"]), None)
        bird_traits = {
            "core_energy": bird_data.get("core_energy", []) if bird_data else [],
            "strengths": bird_data.get("strengths", []) if bird_data else [],
            "challenges": bird_data.get("challenges", []) if bird_data else []
        }
    
    solar_wave_traits = {"core_energy": [], "strengths": [], "challenges": []}
    if elements.get("solar_wave"):
        solar_wave_data = next((g for g in solar_wave_glyphs if g["solar_wave_glyph"] == elements["solar_wave"]), None)
        solar_wave_traits = {
            "core_energy": solar_wave_data.get("core_energy", []) if solar_wave_data else [],
            "strengths": solar_wave_data.get("strengths", []) if solar_wave_data else [],
            "challenges": solar_wave_data.get("challenges", []) if solar_wave_data else []
        }
    
    year_glyph_data = next((y for y in year_glyphs if y["year_glyph"] == elements["year_name"]), None)
    year_glyph_traits = {
        "core_energy": year_glyph_data.get("core_energy", []) if year_glyph_data else [],
        "strengths": year_glyph_data.get("strengths", []) if year_glyph_data else [],
        "challenges": year_glyph_data.get("challenges", []) if year_glyph_data else []
    }
    
    year_number_data = day_numbers.get(str(elements["year_number"]), {})
    year_number_traits = {
        "core_energy": year_number_data.get("core_energy", []),
        "strengths": year_number_data.get("strengths", []),
        "challenges": year_number_data.get("challenges", [])
    }
    
    est_time_str = birth_date.strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "birth_date": est_time_str,
        "elements": elements,
        "day_glyph_traits": day_glyph_traits,
        "day_number_traits": day_number_traits,
        "lord_of_night_traits": lord_of_night_traits,
        "nahual_traits": nahual_traits,
        "lord_of_day_traits": lord_of_day_traits,
        "bird_traits": bird_traits,
        "solar_wave_traits": solar_wave_traits,
        "year_glyph_traits": year_glyph_traits,
        "year_number_traits": year_number_traits
    }

def display_mexica_date(result, user_year, user_month, user_day, final_hour, final_minute):
    local_now = datetime(int(user_year), user_month, user_day, final_hour, final_minute).astimezone()
    formatted_date = local_now.strftime("%A %B %d %Y %I:%M %p")
    print(f"🕒 Birth Date: {formatted_date}")
    print(f"📜 Mexica Year Number: {result['Mexica Year Number']}")
    print(f"🗿 Mexica Year Name: {result['Mexica Year Name']}")
    print()
    
    if "Nemontemi Day Number" in result:
        print(f"🔢 Nemontemi Day Number: {result['Nemontemi Day Number']}")
        print(f"🗿 Nemontemi Day Glyph: {result['Nemontemi Day Glyph']}")
        print(f"🔢 Nemontemi Start Number: {result['Nemontemi Start Number']}")
        print(f"🗿 Nemontemi Start Glyph: {result['Nemontemi Start Glyph']}")
        nemontemi_number_data = day_numbers.get(str(result["Nemontemi Day Number"]), {})
        nemontemi_traits = {
            "core_energy": nemontemi_number_data.get("core_energy", []),
            "strengths": nemontemi_number_data.get("strengths", []),
            "challenges": nemontemi_number_data.get("challenges", [])
        }
        print(f"🔢 Nemontemi Day Number: {result['Nemontemi Day Number']} Traits: {nemontemi_traits}")
        print()
        year_glyph_data = next((y for y in year_glyphs if y["year_glyph"] == result["Mexica Year Name"]), None)
        year_glyph_traits = {
            "core_energy": year_glyph_data.get("core_energy", []) if year_glyph_data else [],
            "strengths": year_glyph_data.get("strengths", []) if year_glyph_data else [],
            "challenges": year_glyph_data.get("challenges", []) if year_glyph_data else []
        }
        print(f"🗿 Year Glyph: {result['Mexica Year Name']} Traits: {year_glyph_traits}")
        print()
        year_number_data = day_numbers.get(str(result["Mexica Year Number"]), {})
        year_number_traits = {
            "core_energy": year_number_data.get("core_energy", []),
            "strengths": year_number_data.get("strengths", []),
            "challenges": year_number_data.get("challenges", [])
        }
        print(f"🔢 Year Number: {result['Mexica Year Number']} Traits: {year_number_traits}")
        print()
    else:
        print(f"🔢 Day Number: {result['Day Number']}")
        print(f"🗿 Day Glyph: {result['Day Glyph']}")
        solar_wave, solar_direction = get_solar_wave(result["Day Number"], result["Day Glyph"])
        print(f"☀️ Solar Wave: {solar_wave}   Direction: {solar_direction}")
        ruler, bird = get_day_ruler_bird(result["Day Number"])
        print(f"👑 Day Ruler: {ruler}")
        print(f"🕊  Bird: {bird}")
        lord_num, lord, nahual = get_lord_night_nahual(result["Group Position"], result["Day Glyph"])
        print(f"👑 Lord of Night: {lord}")
        print(f"🐦 Nahual (Animal): {nahual}")
        print()
        day_glyph_data = next((g for g in day_glyphs_json if g["day_glyph"] == result["Day Glyph"]), None)
        day_glyph_traits = {
            "core_energy": day_glyph_data.get("core_energy", []) if day_glyph_data else [],
            "strengths": day_glyph_data.get("strengths", []) if day_glyph_data else [],
            "challenges": day_glyph_data.get("challenges", []) if day_glyph_data else []
        }
        print(f"🗿 Day Glyph: {result['Day Glyph']} Traits: {day_glyph_traits}")
        print()
        day_number_data = day_numbers.get(str(result["Day Number"]), {})
        day_number_traits = {
            "core_energy": day_number_data.get("core_energy", []),
            "strengths": day_number_data.get("strengths", []),
            "challenges": day_number_data.get("challenges", [])
        }
        print(f"🔢 Day Number: {result['Day Number']} Traits: {day_number_traits}")
        print()
        lord_of_night_data = next((l for l in lords_of_night if l["name"] == lord), None)
        lord_of_night_traits = {
            "core_energy": lord_of_night_data.get("core_energy", []) if lord_of_night_data else [],
            "strengths": lord_of_night_data.get("strengths", []) if lord_of_night_data else [],
            "challenges": lord_of_night_data.get("challenges", []) if lord_of_night_data else []
        }
        print(f"👑 Lord of Night: {lord} Traits: {lord_of_night_traits}")
        print()
        nahual_data = next((n for n in nahuals if n["name"] == nahual), None)
        nahual_traits = {
            "core_energy": nahual_data.get("core_energy", []) if nahual_data else [],
            "strengths": nahual_data.get("strengths", []) if nahual_data else [],
            "challenges": nahual_data.get("challenges", []) if nahual_data else []
        }
        print(f"🐦 Nahual (Animal): {nahual} Traits: {nahual_traits}")
        print()
        lord_of_day_data = next((l for l in lords_of_day if l["name"] == ruler), None)
        lord_of_day_traits = {
            "core_energy": lord_of_day_data.get("core_energy", []) if lord_of_day_data else [],
            "strengths": lord_of_day_data.get("strengths", []) if lord_of_day_data else [],
            "challenges": lord_of_day_data.get("challenges", []) if lord_of_day_data else []
        }
        print(f"👑 Day Ruler: {ruler} Traits: {lord_of_day_traits}")
        print()
        bird_data = next((b for b in birds if b["name"] == bird), None)
        bird_traits = {
            "core_energy": bird_data.get("core_energy", []) if bird_data else [],
            "strengths": bird_data.get("strengths", []) if bird_data else [],
            "challenges": bird_data.get("challenges", []) if bird_data else []
        }
        print(f"🕊  Bird: {bird} Traits: {bird_traits}")
        print()
        solar_wave_data = next((g for g in solar_wave_glyphs if g["solar_wave_glyph"] == solar_wave), None)
        solar_wave_traits = {
            "core_energy": solar_wave_data.get("core_energy", []) if solar_wave_data else [],
            "strengths": solar_wave_data.get("strengths", []) if solar_wave_data else [],
            "challenges": solar_wave_data.get("challenges", []) if solar_wave_data else []
        }
        print(f"☀️ Solar Wave: {solar_wave} Traits: {solar_wave_traits}")
        print()
        year_glyph_data = next((y for y in year_glyphs if y["year_glyph"] == result["Mexica Year Name"]), None)
        year_glyph_traits = {
            "core_energy": year_glyph_data.get("core_energy", []) if year_glyph_data else [],
            "strengths": year_glyph_data.get("strengths", []) if year_glyph_data else [],
            "challenges": year_glyph_data.get("challenges", []) if year_glyph_data else []
        }
        print(f"🗿 Year Glyph: {result['Mexica Year Name']} Traits: {year_glyph_traits}")
        print()
        year_number_data = day_numbers.get(str(result["Mexica Year Number"]), {})
        year_number_traits = {
            "core_energy": year_number_data.get("core_energy", []),
            "strengths": year_number_data.get("strengths", []),
            "challenges": year_number_data.get("challenges", [])
        }
        print(f"🔢 Year Number: {result['Mexica Year Number']} Traits: {year_number_traits}")
        print()

if __name__ == "__main__":
    today = datetime.now(pytz.timezone("America/New_York"))
    today_year = today.year
    today_month = today.month
    today_day = today.day
    today_hour = today.hour
    today_minute = today.minute
    today_result = get_mexica_date(today_year, today_month, today_day, today_hour, today_minute, True)

    print("Today's Mexica Date:")
    display_mexica_date(today_result, today_year, today_month, today_day, today_hour, today_minute)
    print()

    print("Choose an option:")
    print("1. Calculate your birth chart")
    print("2. Generate training data (3000 entries)")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        while True:
            try:
                user_year = input("Enter your birth year (or type 'exit' to quit): ")
                if user_year.lower() == 'exit':
                    print("Goodbye!")
                    break
                user_month = int(input("Enter birth month (1-12): "))
                user_day = int(input("Enter birth day (1-31): "))
                know_time_input = input("Do you know your time of birth? (yes/y/no/n): ").strip().lower()
                while know_time_input not in ['yes', 'y', 'no', 'n']:
                    print("❌ Please enter 'yes', 'y', 'no', or 'n'.")
                    know_time_input = input("Do you know your time of birth? (yes/y/no/n): ").strip().lower()
                time_known = know_time_input in ['yes', 'y']
                if time_known:
                    print("The time zone used to calculate is EST (Eastern Standard Time).")
                    know_tz_input = input("Were you born in a time zone other than EST? (yes/y/no/n): ").strip().lower()
                    while know_tz_input not in ['yes', 'y', 'no', 'n']:
                        print("❌ Please enter 'yes', 'y', 'no', or 'n'.")
                        know_tz_input = input("Were you born in a time zone other than EST? (yes/y/no/n): ").strip().lower()
                    know_tz = know_tz_input in ['yes', 'y']
                    if know_tz:
                        user_tz_abbr = input("Enter your birth time zone (e.g., 'PST', 'CST', 'EST', 'AST_CA', 'NFld'): ").strip().lower()
                        if user_tz_abbr in tz_dict:
                            local_tz = pytz.timezone(tz_dict[user_tz_abbr])
                        else:
                            try:
                                local_tz = pytz.timezone(user_tz_abbr)
                            except pytz.exceptions.UnknownTimeZoneError:
                                print("❌ Unknown time zone. Defaulting to EST (America/New_York).")
                                local_tz = pytz.timezone("America/New_York")
                    else:
                        local_tz = pytz.timezone("America/New_York")
                        print("Assuming your birth time zone is EST (America/New_York).")
                    
                    user_hour = int(input("Enter birth hour (1-12): "))
                    user_minute = int(input("Enter birth minute (0-59): "))
                    am_pm = input("Enter AM or PM: ").strip().upper()
                    if am_pm not in ['AM', 'PM']:
                        raise ValueError("Please enter 'AM' or 'PM'")
                    if user_hour < 1 or user_hour > 12:
                        raise ValueError("Hour must be between 1 and 12")
                    if am_pm == 'PM' and user_hour != 12:
                        user_hour += 12
                    elif am_pm == 'AM' and user_hour == 12:
                        user_hour = 0
                    
                    naive_dt = datetime(int(user_year), user_month, user_day, user_hour, user_minute)
                    est_tz = pytz.timezone("America/New_York")
                    local_dt = est_tz.localize(naive_dt, is_dst=False)
                    if local_tz != est_tz:
                        local_dt = local_dt.astimezone(local_tz)
                    
                    final_hour = local_dt.hour
                    final_minute = local_dt.minute
                else:
                    final_hour, final_minute = 12, 0
                    time_known = True

                result = get_mexica_date(int(user_year), user_month, user_day, final_hour, final_minute, time_known)
                print(f"\nYour Mexica Date:")
                display_mexica_date(result, user_year, user_month, user_day, final_hour, final_minute)
                print()

            except ValueError as e:
                print(f"❌ Invalid input: {e}. Please enter valid values (e.g., hour 1-12, minute 0-59, AM/PM).")
            except pytz.exceptions.UnknownTimeZoneError:
                print("❌ Unknown time zone. Please use a valid time zone (e.g., 'America/New_York', 'America/Mexico_City', 'Europe/London').")
    elif choice == '2':
        generate_training_data(num_entries=3000)
    else:
        print("Goodbye!")
