import pandas as pd
from pathlib import Path
DATA_DIR = Path("data/raw")
for file in DATA_DIR.glob("*.csv"):
    df = pd.read_csv(file)

    print(f"\nDataset: {file.name}")
    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())