import pandas as pd
import random


orders = pd.read_csv(
    "data/raw/orders.csv"
)

products = pd.read_csv(
    "data/raw/products.csv"
)


order_items = []

item_number = 1


for _, order in orders.iterrows():

    if order["order_status"] == "Cancelled":
        continue

    if order["order_status"] == "Completed":
        number_of_products = random.randint(1, 5)
    else:
        number_of_products = random.randint(1, 3)

    selected_products = products.sample(
        n=number_of_products
    )

    for _, product in selected_products.iterrows():

        quantity = random.randint(1, 10)

        unit_price = float(
            product["selling_price"]
        )

        discount_amount = round(
            unit_price
            * quantity
            * random.uniform(0, 0.15),
            2
        )

        order_item = {
            "order_item_id":
                f"ITEM{item_number:07d}",

            "order_id":
                order["order_id"],

            "product_id":
                product["product_id"],

            "quantity":
                quantity,

            "unit_price":
                unit_price,

            "discount_amount":
                discount_amount
        }

        order_items.append(order_item)

        item_number += 1


df_order_items = pd.DataFrame(
    order_items
)


output_path = "data/raw/order_items.csv"

df_order_items.to_csv(
    output_path,
    index=False
)


print(
    f"Created {len(df_order_items)} order items."
)

print(f"Saved to: {output_path}")