import pandas as pd
import random
from datetime import timedelta


purchase_orders = pd.read_csv(
    "data/raw/purchase_orders.csv"
)

suppliers = pd.read_csv(
    "data/raw/suppliers.csv"
)


# Only shipment-worthy purchase orders
eligible_pos = purchase_orders[
    purchase_orders["purchase_order_status"].isin(
        ["Received", "In Transit"]
    )
].copy()


# Limit to approximately 1500
eligible_pos = eligible_pos.sample(
    n=min(1500, len(eligible_pos)),
    random_state=42
)


shipments = []


for i, (_, po) in enumerate(
    eligible_pos.iterrows(),
    start=1
):

    supplier = suppliers[
        suppliers["supplier_id"]
        == po["supplier_id"]
    ].iloc[0]

    origin_country = supplier[
        "supplier_country"
    ]

    shipment_date = pd.to_datetime(
        po["order_date"]
    ) + pd.Timedelta(
        days=random.randint(1, 7)
    )

    estimated_arrival = pd.to_datetime(
        po["expected_delivery_date"]
    )

    delay_days = random.choices(
        [0, 1, 3, 7, 14],
        weights=[55, 20, 15, 8, 2],
        k=1
    )[0]

    actual_arrival = (
        estimated_arrival
        + timedelta(days=delay_days)
    )

    if origin_country == "China":
        shipping_method = random.choice(
            ["Sea Freight", "Rail Freight", "Air Freight"]
        )
    elif origin_country == "India":
        shipping_method = random.choice(
            ["Sea Freight", "Air Freight"]
        )
    else:
        shipping_method = random.choice(
            ["Road Freight", "Courier"]
        )

    freight_cost = round(
        random.uniform(100, 5000),
        2
    )

    if origin_country == "UK":
        import_duty = 0
    else:
        import_duty = round(
            random.uniform(100, 1500),
            2
        )

    other_import_cost = round(
        random.uniform(50, 500),
        2
    )

    if delay_days == 0:
        status = "Delivered"
    else:
        status = random.choice(
            ["Delivered", "Delayed"]
        )

    shipment = {
        "shipment_id": f"SHIP{i:06d}",
        "purchase_order_id":
            po["purchase_order_id"],
        "origin_country": origin_country,
        "destination_country": "UK",
        "shipment_date":
            shipment_date.date(),
        "estimated_arrival_date":
            estimated_arrival.date(),
        "actual_arrival_date":
            actual_arrival.date(),
        "shipping_method": shipping_method,
        "freight_cost": freight_cost,
        "import_duty": import_duty,
        "other_import_cost": other_import_cost,
        "shipment_status": status
    }

    shipments.append(shipment)


df_shipments = pd.DataFrame(shipments)


output_path = "data/raw/shipments.csv"

df_shipments.to_csv(
    output_path,
    index=False
)


print(
    f"Created {len(df_shipments)} shipments."
)

print(f"Saved to: {output_path}")