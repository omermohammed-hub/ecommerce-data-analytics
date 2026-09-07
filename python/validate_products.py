import pandas as pd


df = pd.read_csv("data/raw/products.csv")
suppliers = pd.read_csv("data/raw/suppliers.csv")


print("----- BASIC CHECKS -----")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))


print("\n----- CATEGORIES -----")
print(df["category"].value_counts())


print("\n----- ACTIVE FLAG -----")
print(df["active_flag"].value_counts())


print("\n----- MISSING VALUES -----")
print(df.isnull().sum())


print("\n----- DUPLICATE PRODUCT IDs -----")
print(df["product_id"].duplicated().sum())


print("\n----- INVALID SUPPLIER IDs -----")

invalid_suppliers = ~df["supplier_id"].isin(
    suppliers["supplier_id"]
)

print(invalid_suppliers.sum())


print("\n----- PRICE CHECK -----")

invalid_prices = (
    df["selling_price"] <= df["cost_price"]
)

print(invalid_prices.sum())