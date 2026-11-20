
import pandas as pd

df = pd.read_csv("data/raw/fund_master.csv")

print("Total Schemes:", len(df))

print("\nUnique Fund Houses:")
print(df["fund_house"].value_counts())

print("\nFund Categories:")
print(df["category"].value_counts())

print("\nSub Categories:")
print(df["sub_category"].value_counts())

print("\nRisk Grades:")
print(df["risk_category"].value_counts())

print("\nAMFI Scheme Code Examples:")
print(df[["amfi_code", "scheme_name"]].head(10))
