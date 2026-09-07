import pandas as pd
import random


# --------------------------------------------------
# 1. Load source tables
# --------------------------------------------------

products = pd.read_csv(
    "data/raw/products.csv"
)

purchase_orders = pd.read_csv(
    "data/raw/purchase_orders.csv"
)

order_items = pd.read_csv(
    "data/raw/order_items.csv"
)

orders = pd.read_csv(
    "data/raw/orders.csv"
)

returns = pd.read_csv(
    "data/raw/returns.csv"
)


# --------------------------------------------------
# 2. Prepare completed sales
# --------------------------------------------------

completed_order_ids = set(
    orders.loc[
        orders["order_status"] == "Completed",
        "order_id"
    ]
)

sales = order_items[
    order_items["order_id"].isin(
        completed_order_ids
    )
].copy()


# --------------------------------------------------
# 3. Prepare received purchase orders
# --------------------------------------------------

received_pos = purchase_orders[
    purchase_orders["purchase_order_status"] == "Received"
].copy()


# --------------------------------------------------
# 4. Prepare approved returns
# --------------------------------------------------

approved_returns = returns[
    returns["return_status"] == "Approved"
].copy()


# --------------------------------------------------
# 5. Aggregate movements by product
# --------------------------------------------------

sales_by_product = (
    sales
    .groupby("product_id")["quantity"]
    .sum()
)

received_by_product = (
    received_pos
    .groupby("product_id")["quantity_ordered"]
    .sum()
)

returns_by_product = (
    approved_returns
    .groupby("product_id")["quantity_returned"]
    .sum()
)


# --------------------------------------------------
# 6. Generate monthly inventory
# --------------------------------------------------

inventory = []

inventory_number = 1


for _, product in products.iterrows():

    product_id = product["product_id"]

    # Total annual movements for this product
    total_received = int(
        received_by_product.get(
            product_id,
            0
        )
    )

    total_sold = int(
        sales_by_product.get(
            product_id,
            0
        )
    )

    total_returned = int(
        returns_by_product.get(
            product_id,
            0
        )
    )


    # --------------------------------------------------
    # Starting stock
    # --------------------------------------------------

    opening_stock = random.randint(
        50,
        250
    )


    # --------------------------------------------------
    # Create monthly movements
    # --------------------------------------------------

    for month in range(1, 13):

        # Spread annual movements approximately
        # across the 12 months.
        base_received = total_received // 12
        base_sold = total_sold // 12
        base_returned = total_returned // 12


        # Add the remainder to the final month
        if month == 12:

            monthly_received = (
                base_received
                + total_received % 12
            )

            monthly_sold = (
                base_sold
                + total_sold % 12
            )

            monthly_returned = (
                base_returned
                + total_returned % 12
            )

        else:

            monthly_received = base_received
            monthly_sold = base_sold
            monthly_returned = base_returned


        # --------------------------------------------------
        # Prevent sales from exceeding available stock
        # --------------------------------------------------

        available_stock = (
            opening_stock
            + monthly_received
            + monthly_returned
        )

        monthly_sold = min(
            monthly_sold,
            available_stock
        )


        # --------------------------------------------------
        # Calculate closing stock
        # --------------------------------------------------

        closing_stock = (
            opening_stock
            + monthly_received
            - monthly_sold
            + monthly_returned
        )


        # --------------------------------------------------
        # Store inventory record
        # --------------------------------------------------

        inventory_record = {

            "inventory_id":
                f"INV{inventory_number:07d}",

            "product_id":
                product_id,

            "inventory_date":
                f"2025-{month:02d}-28",

            "opening_stock":
                opening_stock,

            "units_received":
                monthly_received,

            "units_sold":
                monthly_sold,

            "units_returned":
                monthly_returned,

            "closing_stock":
                closing_stock
        }


        inventory.append(
            inventory_record
        )


        # The next month's opening stock
        # must equal this month's closing stock.
        opening_stock = closing_stock

        inventory_number += 1


# --------------------------------------------------
# 7. Create DataFrame
# --------------------------------------------------

df_inventory = pd.DataFrame(
    inventory
)


# --------------------------------------------------
# 8. Save CSV
# --------------------------------------------------

output_path = "data/raw/inventory.csv"

df_inventory.to_csv(
    output_path,
    index=False
)


# --------------------------------------------------
# 9. Display result
# --------------------------------------------------

print(
    f"Created {len(df_inventory)} inventory records."
)

print(
    f"Saved to: {output_path}"
)