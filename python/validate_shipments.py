import pandas as pd


df = pd.read_csv(
    "data/raw/shipments.csv"
)

purchase_orders = pd.read_csv(
    "data/raw/purchase_orders.csv"
)


print("----- BASIC CHECKS -----")

print("Rows:", len(df))
print("Columns:", len(df.columns))


print("\n----- ORIGIN COUNTRY -----")

print(
    df["origin_country"].value_counts()
)


print("\n----- SHIPPING METHOD -----")

print(
    df["shipping_method"].value_counts()
)


print("\n----- STATUS -----")

print(
    df["shipment_status"].value_counts()
)


print("\n----- MISSING VALUES -----")

print(df.isnull().sum())


print("\n----- DUPLICATE SHIPMENT IDs -----")

print(
    df["shipment_id"].duplicated().sum()
)


print("\n----- INVALID PURCHASE ORDER IDs -----")

print(
    (~df["purchase_order_id"].isin(
        purchase_orders["purchase_order_id"]
    )).sum()
)