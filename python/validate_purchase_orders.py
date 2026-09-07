import pandas as pd


df = pd.read_csv(
    "data/raw/purchase_orders.csv"
)

products = pd.read_csv(
    "data/raw/products.csv"
)

suppliers = pd.read_csv(
    "data/raw/suppliers.csv"
)


print("----- BASIC CHECKS -----")

print("Rows:", len(df))
print("Columns:", len(df.columns))


print("\n----- STATUS -----")

print(
    df["purchase_order_status"]
    .value_counts()
)


print("\n----- MISSING VALUES -----")

print(df.isnull().sum())


print("\n----- DUPLICATE PO IDs -----")

print(
    df["purchase_order_id"].duplicated().sum()
)


print("\n----- INVALID PRODUCT IDs -----")

print(
    (~df["product_id"].isin(
        products["product_id"]
    )).sum()
)


print("\n----- INVALID SUPPLIER IDs -----")

print(
    (~df["supplier_id"].isin(
        suppliers["supplier_id"]
    )).sum()
)


print("\n----- INVALID QUANTITIES -----")

print(
    (df["quantity_ordered"] <= 0).sum()
)