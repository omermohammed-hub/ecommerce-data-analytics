import pandas as pd
import random
from datetime import timedelta


products = pd.read_csv("data/raw/products.csv")
suppliers = pd.read_csv("data/raw/suppliers.csv")


purchase_orders = []


for i in range(1, 2001):

    product = products.sample(1).iloc[0]

    supplier_id = product["supplier_id"]

    supplier = suppliers[
        suppliers["supplier_id"] == supplier_id
    ].iloc[0]

    order_date = pd.Timestamp(
        "2025-01-01"
    ) + pd.Timedelta(
        days=random.randint(0, 570)
    )

    lead_time = int(
        supplier["standard_lead_time_days"]
    )

    expected_delivery_date = (
        order_date
        + timedelta(days=lead_time)
    )

    quantity_ordered = random.randint(
        20, 1000
    )

    unit_cost = float(
        product["cost_price"]
    )

    status = random.choices(
        [
            "Received",
            "In Transit",
            "Cancelled"
        ],
        weights=[75, 20, 5],
        k=1
    )[0]

    purchase_order = {
        "purchase_order_id": f"PO{i:06d}",
        "supplier_id": supplier_id,
        "product_id": product["product_id"],
        "order_date": order_date.date(),
        "expected_delivery_date":
            expected_delivery_date.date(),
        "quantity_ordered": quantity_ordered,
        "unit_cost": unit_cost,
        "purchase_order_status": status
    }

    purchase_orders.append(purchase_order)


df_purchase_orders = pd.DataFrame(
    purchase_orders
)


output_path = "data/raw/purchase_orders.csv"

df_purchase_orders.to_csv(
    output_path,
    index=False
)


print(
    f"Created {len(df_purchase_orders)} purchase orders."
)

print(f"Saved to: {output_path}")