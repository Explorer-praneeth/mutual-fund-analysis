
import requests
import pandas as pd
from pathlib import Path

# Mutual fund scheme codes
SCHEMES = {
    "HDFC Top 100": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

all_nav_data = []

for fund_name, scheme_code in SCHEMES.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    result = response.json()

    df = pd.DataFrame(result["data"])
    df["scheme_code"] = scheme_code
    df["fund_name"] = fund_name

    all_nav_data.append(df)

    print(f"{fund_name}: {len(df)} NAV records fetched")

# Combine all funds
nav_history = pd.concat(all_nav_data, ignore_index=True)

# Save raw NAV data
nav_history.to_csv(
    output_dir / "nav_history.csv",
    index=False
)

print("\nCombined NAV shape:", nav_history.shape)
print(nav_history.head())
