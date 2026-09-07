import pandas as pd
import random


orders = pd.read_csv(
    "data/raw/orders.csv"
)

order_items = pd.read_csv(
    "data/raw/order_items.csv"
)


# Calculate order value
order_items["gross_sales"] = (
    order_items["quantity"]
    * order_items["unit_price"]
)

order_items["net_sales"] = (
    order_items["gross_sales"]
    - order_items["discount_amount"]
)


order_totals = (
    order_items
    .groupby("order_id")["net_sales"]
    .sum()
    .reset_index()
)


orders = orders.merge(
    order_totals,
    on="order_id",
    how="left"
)

orders["net_sales"] = (
    orders["net_sales"].fillna(0)
)


payments = []


payment_number = 1


for _, order in orders.iterrows():

    if order["order_status"] == "Cancelled":
        continue

    if order["net_sales"] <= 0:
        continue

    payment_method = random.choices(
        [
            "Card",
            "PayPal",
            "Apple Pay",
            "Google Pay",
            "Bank Transfer"
        ],
        weights=[55, 15, 10, 10, 10],
        k=1
    )[0]

    if order["order_status"] == "Completed":

        payment_status = random.choices(
            ["Paid", "Failed"],
            weights=[97, 3],
            k=1
        )[0]

    else:

        payment_status = random.choice(
            ["Paid", "Pending"]
        )

    payment = {
        "payment_id":
            f"PAY{payment_number:07d}",

        "order_id":
            order["order_id"],

        "payment_date":
            order["order_date"],

        "payment_method":
            payment_method,

        "payment_status":
            payment_status,

        "amount":
            round(float(order["net_sales"]), 2)
    }

    payments.append(payment)

    payment_number += 1


df_payments = pd.DataFrame(payments)


output_path = "data/raw/payments.csv"

df_payments.to_csv(
    output_path,
    index=False
)


print(
    f"Created {len(df_payments)} payments."
)

print(f"Saved to: {output_path}")