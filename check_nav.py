import pandas as pd

df = pd.read_csv("data/raw/nav_history.csv")

print("Shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:", df.duplicated().sum())

print("\nFund-wise records:")
print(df.groupby("fund_name").size())
master = pd.read_csv("data/raw/fund_master.csv")

print("\nFund master scheme codes:")
print(master.columns.tolist())
master = pd.read_csv("data/raw/fund_master.csv")

master_codes = set(master["amfi_code"].astype(str))
nav_codes = set(df["scheme_code"].astype(str))

missing_codes = master_codes - nav_codes

print("\nFund master codes:", len(master_codes))
print("NAV scheme codes:", len(nav_codes))
print("Missing NAV codes:", missing_codes)

if not missing_codes:
    print("All fund master codes exist in NAV history.")