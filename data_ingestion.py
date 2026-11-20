
import pandas as pd
from pathlib import Path

# Project data directory
DATA_DIR = Path("data/raw")

# All 10 datasets
datasets = [
    "fund_master.csv",
    "nav_history.csv",
    "aum_by_fund_house.csv",
    "monthly_sip_inflows.csv",
    "category_inflows.csv",
    "industry_folio_count.csv",
    "scheme_performance.csv",
    "investor_transactions.csv",
    "portfolio_holdings.csv",
    "benchmark_indices.csv"
]

# Load and inspect datasets
for file in datasets:

    file_path = DATA_DIR / file

    print("\n" + "=" * 70)
    print(f"DATASET: {file}")
    print("=" * 70)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error loading {file}: {e}")

print("\nAll dataset inspections completed!")
missing = df.isnull().sum()

if missing.sum() > 0:
    print("\nColumns with missing values:")
    print(missing[missing > 0])
else:
    print("\nNo missing values found.")