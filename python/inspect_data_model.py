import pandas as pd
from pathlib import Path


# Location of the raw CSV files
DATA_DIR = Path("data/raw")


# All tables we want to inspect
tables = [
    "customers",
    "suppliers",
    "products",
    "purchase_orders",
    "shipments",
    "orders",
    "order_items",
    "payments",
    "returns",
    "inventory"
]


print("=" * 70)
print("E-COMMERCE DATA MODEL INSPECTION")
print("=" * 70)


for table in tables:

    file_path = DATA_DIR / f"{table}.csv"

    print("\n")
    print("=" * 70)
    print(f"TABLE: {table.upper()}")
    print("=" * 70)

    # Load the CSV
    df = pd.read_csv(file_path)

    # Basic structure
    print("\n----- BASIC STRUCTURE -----")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    # Column information
    print("\n----- COLUMN INFORMATION -----")

    for column in df.columns:

        print(
            f"{column:<30}"
            f"Type: {str(df[column].dtype):<12}"
            f"Nulls: {df[column].isnull().sum():<6}"
            f"Unique: {df[column].nunique()}"
        )

    # Duplicate rows
    print("\n----- DUPLICATE ROWS -----")
    print("Duplicate rows:", df.duplicated().sum())

    # Sample records
    print("\n----- SAMPLE RECORD -----")
    print(df.head(2).to_string(index=False))


print("\n")
print("=" * 70)
print("INSPECTION COMPLETE")
print("=" * 70)