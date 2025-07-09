from datetime import datetime
from src.checker import evaluate_mpin

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Prompt for valid MPIN
while True:
    mpin = input("Enter MPIN (4 or 6 digits): ").strip()
    if mpin.isdigit() and len(mpin) in [4, 6]:
        break
    print("Please enter a valid MPIN containing exactly 4 or 6 digits.\n")

# Ask for additional details
dob = input("Enter your Date of Birth (YYYY-MM-DD): ").strip()
spouse_dob = input("Enter Spouse's Date of Birth (YYYY-MM-DD): ").strip()
anniversary = input("Enter Anniversary Date (YYYY-MM-DD): ").strip()

# Check for missing inputs
if not dob or not spouse_dob or not anniversary:
    print("All details are required. Please provide complete information.")
    exit()

# Validate all dates
for label, value in [("Date of Birth", dob), ("Spouse's Date of Birth", spouse_dob), ("Anniversary Date", anniversary)]:
    if not is_valid_date(value):
        print(f"Invalid {label}. Please use the format YYYY-MM-DD.")
        exit()

# Evaluate MPIN
result = evaluate_mpin(mpin, dob, spouse_dob, anniversary)

# Friendly label mapping
reason_labels = {
    "COMMONLY_USED": "MPIN is commonly used by many users.",
    "DEMOGRAPHIC_DOB_SELF": "MPIN is similar to your Date of Birth.",
    "DEMOGRAPHIC_DOB_SPOUSE": "MPIN is similar to your Spouse's Date of Birth.",
    "DEMOGRAPHIC_ANNIVERSARY": "MPIN is similar to your Anniversary Date."
}

# Display result
print("\nMPIN Evaluation Result:")
if result["strength"] == "WEAK":
    print("Your MPIN is considered WEAK due to the following reason(s):")
    for reason in result["reasons"]:
        print(f"- {reason_labels.get(reason, reason)}")
else:
    print("MPIN is STRONG.")

print("\nThank you for using the MPIN Strength Checker.")
