from datetime import datetime
import os

# --- Load Common MPINs from File ---
def load_common_mpins(filepath: str) -> set:
    if not os.path.exists(filepath):
        return set()
    with open(filepath, "r") as f:
        return set(line.strip() for line in f if line.strip())

COMMON_MPINS = load_common_mpins("data/common_mpins.txt")

# --- Check if MPIN is Common ---
def is_common_mpin(mpin: str) -> bool:
    return mpin in COMMON_MPINS

# --- Extract Patterns from Date ---
def extract_date_patterns(date_str: str) -> set:
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return set()

    day = f"{dt.day:02d}"
    month = f"{dt.month:02d}"
    year_full = str(dt.year)
    year_short = year_full[2:]

    return {
        day + month,
        month + day,
        year_short + month,
        month + year_short,
        day + year_short,
        year_short + day,
        year_short,
        year_full,
        day + month + year_short,
        month + day + year_short,
        year_short + month + day,
        year_short + day + month,
        year_short + month + day,
        year_full + day,
        day + month + year_full,
        day[::-1] + year_short,    # Reverse DD → 30 + 99 = 3099
        year_short + day[::-1], 
        month[::-1] + year_short,  
    }

# --- Evaluate MPIN Against All Checks ---
def evaluate_mpin(mpin: str, dob: str, spouse_dob: str, anniversary: str) -> dict:
    reasons = []

    if is_common_mpin(mpin):
        reasons.append("COMMONLY_USED")

    patterns_by_label = {
        "DEMOGRAPHIC_DOB_SELF": extract_date_patterns(dob),
        "DEMOGRAPHIC_DOB_SPOUSE": extract_date_patterns(spouse_dob),
        "DEMOGRAPHIC_ANNIVERSARY": extract_date_patterns(anniversary),
    }

    for label, patterns in patterns_by_label.items():
        if mpin in patterns:
            reasons.append(label)

    return {
        "strength": "WEAK" if reasons else "STRONG",
        "reasons": reasons
    }

# --- Optional Boolean Match Checker ---
def is_demographic_match(mpin: str, dob: str, spouse_dob: str, anniversary: str) -> bool:
    all_patterns = set()
    for date in [dob, spouse_dob, anniversary]:
        all_patterns.update(extract_date_patterns(date))
    return mpin in all_patterns
