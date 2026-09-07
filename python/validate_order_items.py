import pandas as pd


df = pd.read_csv(
    "data/raw/order_items.csv"
)

orders = pd.read_csv(
    "data/raw/orders.csv"
)

products = pd.read_csv(
    "data/raw/products.csv"
)


print("----- BASIC CHECKS -----")

print("Rows:", len(df))
print("Columns:", len(df.columns))


print("\n----- MISSING VALUES -----")

print(df.isnull().sum())


print("\n----- DUPLICATE ITEM IDs -----")

print(
    df["order_item_id"].duplicated().sum()
)


print("\n----- INVALID ORDER IDs -----")

print(
    (~df["order_id"].isin(
        orders["order_id"]
    )).sum()
)


print("\n----- INVALID PRODUCT IDs -----")

print(
    (~df["product_id"].isin(
        products["product_id"]
    )).sum()
)


print("\n----- INVALID QUANTITIES -----")

print(
    (df["quantity"] <= 0).sum()
)


print("\n----- INVALID PRICES -----")

print(
    (df["unit_price"] <= 0).sum()
)