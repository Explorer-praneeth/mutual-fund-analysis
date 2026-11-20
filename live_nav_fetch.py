import requests
import pandas as pd
from pathlib import Path

master = pd.read_csv("data/raw/fund_master.csv")

all_nav_data = []
failed_codes = []

for _, row in master.iterrows():
    code = str(row["amfi_code"]).replace(".0", "")

    try:
        url = f"https://api.mfapi.in/mf/{code}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        result = response.json()
        df = pd.DataFrame(result["data"])

        if df.empty:
            failed_codes.append(code)
            continue

        df["scheme_code"] = code
        df["fund_name"] = row["scheme_name"]

        all_nav_data.append(df)
        print(f"Fetched: {row['scheme_name']}")

    except Exception as e:
        failed_codes.append(code)
        print(f"Failed: {code} - {e}")

if all_nav_data:
    nav_history = pd.concat(all_nav_data, ignore_index=True)
    nav_history.to_csv("data/raw/nav_history.csv", index=False)

print("\nTotal schemes fetched:", len(all_nav_data))
print("Failed scheme codes:", failed_codes)