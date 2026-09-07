import pandas as pd
import random


order_items = pd.read_csv(
    "data/raw/order_items.csv"
)

orders = pd.read_csv(
    "data/raw/orders.csv"
)


# Only completed orders can have returns
completed_orders = orders[
    orders["order_status"] == "Completed"
]["order_id"]


eligible_items = order_items[
    order_items["order_id"].isin(
        completed_orders
    )
].copy()


# Approximately 5% of eligible items returned
return_count = int(
    len(eligible_items) * 0.05
)

return_items = eligible_items.sample(
    n=return_count,
    random_state=42
)


return_reasons = [
    "Damaged",
    "Wrong Item",
    "Changed Mind",
    "Not as Described",
    "Quality Issue",
    "Late Delivery",
    "Other"
]


returns = []


for i, (_, item) in enumerate(
    return_items.iterrows(),
    start=1
):

    quantity_returned = random.randint(
        1,
        int(item["quantity"])
    )

    refund_amount = round(
        quantity_returned
        * float(item["unit_price"]),
        2
    )

    return_date = (
        pd.Timestamp("2025-01-01")
        + pd.Timedelta(
            days=random.randint(30, 570)
        )
    )

    return_record = {
        "return_id":
            f"RET{i:06d}",

        "order_id":
            item["order_id"],

        "product_id":
            item["product_id"],

        "return_date":
            return_date.date(),

        "quantity_returned":
            quantity_returned,

        "return_reason":
            random.choice(return_reasons),

        "refund_amount":
            refund_amount,

        "return_status":
            random.choices(
                ["Approved", "Rejected", "Pending"],
                weights=[85, 5, 10],
                k=1
            )[0]
    }

    returns.append(return_record)


df_returns = pd.DataFrame(returns)


output_path = "data/raw/returns.csv"

df_returns.to_csv(
    output_path,
    index=False
)


print(
    f"Created {len(df_returns)} returns."
)

print(f"Saved to: {output_path}")