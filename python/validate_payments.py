import pandas as pd


df = pd.read_csv(
    "data/raw/payments.csv"
)

orders = pd.read_csv(
    "data/raw/orders.csv"
)


print("----- BASIC CHECKS -----")

print("Rows:", len(df))
print("Columns:", len(df.columns))


print("\n----- PAYMENT METHODS -----")

print(
    df["payment_method"].value_counts()
)


print("\n----- PAYMENT STATUS -----")

print(
    df["payment_status"].value_counts()
)


print("\n----- MISSING VALUES -----")

print(df.isnull().sum())


print("\n----- DUPLICATE PAYMENT IDs -----")

print(
    df["payment_id"].duplicated().sum()
)


print("\n----- INVALID ORDER IDs -----")

print(
    (~df["order_id"].isin(
        orders["order_id"]
    )).sum()
)


print("\n----- INVALID PAYMENT AMOUNTS -----")

print(
    (df["amount"] <= 0).sum()
)