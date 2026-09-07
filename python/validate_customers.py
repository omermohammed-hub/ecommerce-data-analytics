import pandas as pd

# Load the generated customer data
df = pd.read_csv("data/raw/customers.csv")

print("----- BASIC CHECKS -----")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\n----- COLUMN NAMES -----")
print(df.columns.tolist())

print("\n----- CUSTOMER TYPE -----")
print(df["customer_type"].value_counts())

print("\n----- CUSTOMER TYPE % -----")
print(df["customer_type"].value_counts(normalize=True).mul(100).round(2))

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

print("\n----- DUPLICATE CUSTOMER IDs -----")
print(df["customer_id"].duplicated().sum())