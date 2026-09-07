import pandas as pd


df = pd.read_csv(
    "data/raw/inventory.csv"
)

products = pd.read_csv(
    "data/raw/products.csv"
)


print("----- BASIC CHECKS -----")

print("Rows:", len(df))
print("Columns:", len(df.columns))


print("\n----- PRODUCTS -----")

print(
    df["product_id"].nunique()
)


print("\n----- MISSING VALUES -----")

print(df.isnull().sum())


print("\n----- DUPLICATE INVENTORY IDs -----")

print(
    df["inventory_id"].duplicated().sum()
)


print("\n----- INVALID PRODUCT IDs -----")

print(
    (~df["product_id"].isin(
        products["product_id"]
    )).sum()
)


print("\n----- NEGATIVE STOCK -----")

print(
    (df["closing_stock"] < 0).sum()
)


print("\n----- STOCK CALCULATION CHECK -----")

calculated_closing = (
    df["opening_stock"]
    + df["units_received"]
    - df["units_sold"]
    + df["units_returned"]
)

print(
    (
        calculated_closing
        != df["closing_stock"]
    ).sum()
)
print("\n----- INVENTORY CONTINUITY CHECK -----")

# Make sure the data is in the correct order
df = df.sort_values(
    ["product_id", "inventory_date"]
).reset_index(drop=True)

# Previous month's closing stock
previous_closing_stock = (
    df.groupby("product_id")["closing_stock"]
    .shift(1)
)

# Compare previous month's closing stock
# with current month's opening stock
continuity_errors = (
    previous_closing_stock.notna()
    &
    (
        df["opening_stock"]
        != previous_closing_stock
    )
).sum()

print(
    "Opening stock does not match previous month's closing stock:",
    continuity_errors
)