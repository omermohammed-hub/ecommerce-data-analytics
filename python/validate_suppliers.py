import pandas as pd


# Load supplier data
df = pd.read_csv("data/raw/suppliers.csv")


print("----- BASIC CHECKS -----")

print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))


print("\n----- COLUMN NAMES -----")

print(df.columns.tolist())


print("\n----- SUPPLIERS BY COUNTRY -----")

print(df["supplier_country"].value_counts())


print("\n----- SUPPLIER STATUS -----")

print(df["supplier_status"].value_counts())


print("\n----- LEAD TIME BY COUNTRY -----")

print(
    df.groupby("supplier_country")["standard_lead_time_days"]
      .agg(["min", "max", "mean"])
      .round(2)
)


print("\n----- MISSING VALUES -----")

print(df.isnull().sum())


print("\n----- DUPLICATE SUPPLIER IDs -----")

print(df["supplier_id"].duplicated().sum())