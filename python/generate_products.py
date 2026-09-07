import pandas as pd
import random


# --------------------------------------------------
# 1. Load suppliers
# --------------------------------------------------

suppliers = pd.read_csv("data/raw/suppliers.csv")

supplier_ids = suppliers["supplier_id"].tolist()


# --------------------------------------------------
# 2. Product configuration
# --------------------------------------------------

product_config = {
    "Homeware": [
        "Storage",
        "Kitchen",
        "Cleaning",
        "Bathroom"
    ],
    "Garden & Outdoor": [
        "Garden Tools",
        "Outdoor Furniture",
        "Plant Care",
        "BBQ"
    ],
    "Paints & Decorating": [
        "Interior Paint",
        "Exterior Paint",
        "Brushes & Rollers",
        "Wallpaper"
    ],
    "Electrical": [
        "Lighting",
        "Cables",
        "Switches",
        "Small Electrical"
    ],
    "Health & Beauty": [
        "Personal Care",
        "Hair Care",
        "Skincare",
        "Wellness"
    ],
    "Pet Care": [
        "Dog Care",
        "Cat Care",
        "Pet Food",
        "Pet Accessories"
    ]
}


brands = [
    "HomePro",
    "ValuePlus",
    "Everyday Essentials",
    "PrimeChoice",
    "TradeSelect",
    "SmartBuy"
]


# --------------------------------------------------
# 3. Generate products
# --------------------------------------------------

products = []

for i in range(1, 501):

    category = random.choice(list(product_config.keys()))

    subcategory = random.choice(
        product_config[category]
    )

    brand = random.choice(brands)

    supplier_id = random.choice(supplier_ids)

    cost_price = round(
        random.uniform(2.50, 120.00),
        2
    )

    markup = random.uniform(1.20, 2.00)

    selling_price = round(
        cost_price * markup,
        2
    )

    reorder_level = random.randint(10, 100)

    active_flag = random.choices(
        [True, False],
        weights=[95, 5],
        k=1
    )[0]

    product = {
        "product_id": f"PROD{i:05d}",
        "product_name": f"{brand} {subcategory} Product {i:03d}",
        "category": category,
        "subcategory": subcategory,
        "brand": brand,
        "supplier_id": supplier_id,
        "sourcing_country": suppliers.loc[
            suppliers["supplier_id"] == supplier_id,
            "supplier_country"
        ].iloc[0],
        "cost_price": cost_price,
        "selling_price": selling_price,
        "reorder_level": reorder_level,
        "active_flag": active_flag
    }

    products.append(product)


# --------------------------------------------------
# 4. DataFrame
# --------------------------------------------------

df_products = pd.DataFrame(products)


# --------------------------------------------------
# 5. Save
# --------------------------------------------------

output_path = "data/raw/products.csv"

df_products.to_csv(
    output_path,
    index=False
)

print(f"Created {len(df_products)} products.")
print(f"Saved to: {output_path}")