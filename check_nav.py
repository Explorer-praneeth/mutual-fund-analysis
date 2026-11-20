
import pandas as pd

# Load datasets
nav = pd.read_csv("data/raw/nav_history.csv")
master = pd.read_csv("data/raw/fund_master.csv")

# 1. Basic NAV inspection
print("NAV Dataset Shape:", nav.shape)

print("\nMissing Values:")
print(nav.isnull().sum())

print("\nDuplicate Rows:", nav.duplicated().sum())

# 2. Fund-wise NAV record count
print("\nFund-wise NAV Records:")
print(nav.groupby("amfi_code").size())

# 3. Validate AMFI scheme codes
master_codes = set(
    pd.to_numeric(master["amfi_code"], errors="coerce")
    .dropna().astype("int64")
)

nav_codes = set(
    pd.to_numeric(nav["amfi_code"], errors="coerce")
    .dropna().astype("int64")
)

missing_codes = master_codes - nav_codes
extra_codes = nav_codes - master_codes

print("\n========== AMFI CODE VALIDATION ==========")

print("Fund Master Codes:", len(master_codes))
print("NAV Scheme Codes:", len(nav_codes))

print("\nMissing NAV Codes:", missing_codes)
print("Extra NAV Codes:", extra_codes)

# 4. Check duplicate scheme-date combinations
duplicate_dates = nav.duplicated(
    subset=["amfi_code", "date"]
).sum()

print("\nDuplicate Scheme-Date Records:", duplicate_dates)

# 5. Final result
if not missing_codes and not extra_codes:
    print("\nSUCCESS: All AMFI codes match!")
else:
    print("\nWARNING: AMFI code mismatches found.")
