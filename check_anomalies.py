
import pandas as pd

df = pd.read_csv("data/raw/monthly_sip_inflows.csv")

print("Missing Values:")
print(df.isnull().sum())

print("\nHighest New SIP Accounts:")
print(df.nlargest(5, "new_sip_accounts_lakh")[
    ["month", "new_sip_accounts_lakh"]
])

print("\nHighest SIP Inflows:")
print(df.nlargest(5, "sip_inflow_crore")[
    ["month", "sip_inflow_crore"]
])

print("\nSIP AUM Changes:")
df["aum_change"] = df["sip_aum_lakh_crore"].diff()

print(df[["month", "sip_aum_lakh_crore", "aum_change"]])
