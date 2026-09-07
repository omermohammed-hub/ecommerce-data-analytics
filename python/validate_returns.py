import pandas as pd


df = pd.read_csv(
    "data/raw/returns.csv"
)

orders = pd.read_csv(
    "data/raw/orders.csv"
)

order_items = pd.read_csv(
    "data/raw/order_items.csv"
)


print("----- BASIC CHECKS -----")

print("Rows:", len(df))
print("Columns:", len(df.columns))


print("\n----- RETURN REASONS -----")

print(
    df["return_reason"].value_counts()
)


print("\n----- RETURN STATUS -----")

print(
    df["return_status"].value_counts()
)


print("\n----- MISSING VALUES -----")

print(df.isnull().sum())


print("\n----- DUPLICATE RETURN IDs -----")

print(
    df["return_id"].duplicated().sum()
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
        order_items["product_id"]
    )).sum()
)


print("\n----- INVALID QUANTITY -----")

print(
    (df["quantity_returned"] <= 0).sum()
)


print("\n----- INVALID REFUND -----")

print(
    (df["refund_amount"] <= 0).sum()
)
print("\n----- RETURN PRODUCT-ORDER RELATIONSHIP CHECK -----")

# Create valid order-product combinations
valid_order_products = set(
    zip(
        order_items["order_id"],
        order_items["product_id"]
    )
)

# Create order-product combinations from returns
return_order_products = list(
    zip(
        df["order_id"],
        df["product_id"]
    )
)

# Count returns where the product was NOT part
# of the original order
invalid_return_relationships = sum(
    pair not in valid_order_products
    for pair in return_order_products
)

print(
    "Returns for products not present in the original order:",
    invalid_return_relationships
)