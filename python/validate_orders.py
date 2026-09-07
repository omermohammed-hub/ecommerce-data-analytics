import pandas as pd


df = pd.read_csv(
    "data/raw/orders.csv"
)

customers = pd.read_csv(
    "data/raw/customers.csv"
)


print("----- BASIC CHECKS -----")

print("Rows:", len(df))
print("Columns:", len(df.columns))


print("\n----- ORDER STATUS -----")

print(
    df["order_status"].value_counts()
)


print("\n----- SALES CHANNEL -----")

print(
    df["sales_channel"].value_counts()
)


print("\n----- MISSING VALUES -----")

print(df.isnull().sum())


print("\n----- DUPLICATE ORDER IDs -----")

print(
    df["order_id"].duplicated().sum()
)


print("\n----- INVALID CUSTOMER IDs -----")

print(
    (~df["customer_id"].isin(
        customers["customer_id"]
    )).sum()
)