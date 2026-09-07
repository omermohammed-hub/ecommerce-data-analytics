import pandas as pd
import random
from datetime import timedelta


customers = pd.read_csv(
    "data/raw/customers.csv"
)


orders = []


statuses = [
    "Completed",
    "Cancelled",
    "Pending",
    "Partially Fulfilled"
]


channels = [
    "Online",
    "Marketplace",
    "Trade Counter"
]


delivery_methods = [
    "Home Delivery",
    "Click & Collect",
    "Courier"
]


for i in range(1, 50001):

    customer = customers.sample(
        1
    ).iloc[0]

    order_date = pd.Timestamp(
        "2025-01-01"
    ) + pd.Timedelta(
        days=random.randint(0, 570),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )

    status = random.choices(
        statuses,
        weights=[82, 5, 5, 8],
        k=1
    )[0]

    channel = random.choices(
        channels,
        weights=[70, 20, 10],
        k=1
    )[0]

    delivery_method = random.choice(
        delivery_methods
    )

    order = {
        "order_id": f"ORD{i:06d}",
        "customer_id":
            customer["customer_id"],
        "order_date": order_date,
        "order_status": status,
        "sales_channel": channel,
        "delivery_method": delivery_method,
        "shipping_region":
            customer["region"]
    }

    orders.append(order)


df_orders = pd.DataFrame(orders)


output_path = "data/raw/orders.csv"

df_orders.to_csv(
    output_path,
    index=False
)


print(f"Created {len(df_orders)} orders.")
print(f"Saved to: {output_path}")