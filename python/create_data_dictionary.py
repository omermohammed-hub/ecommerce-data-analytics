import pandas as pd
from pathlib import Path


# ---------------------------------------------------------
# DATA DICTIONARY GENERATOR
# ---------------------------------------------------------

DATA_DIR = Path("data/raw")
OUTPUT_DIR = Path("data/profiling")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


tables = [
    "customers",
    "suppliers",
    "products",
    "purchase_orders",
    "shipments",
    "orders",
    "order_items",
    "payments",
    "returns",
    "inventory"
]


# Expected PK/FK information from our agreed data model
key_roles = {

    "customers": {
        "customer_id": "PK"
    },

    "suppliers": {
        "supplier_id": "PK"
    },

    "products": {
        "product_id": "PK",
        "supplier_id": "FK → suppliers.supplier_id"
    },

    "purchase_orders": {
        "purchase_order_id": "PK",
        "supplier_id": "FK → suppliers.supplier_id",
        "product_id": "FK → products.product_id"
    },

    "shipments": {
        "shipment_id": "PK",
        "purchase_order_id": "FK → purchase_orders.purchase_order_id"
    },

    "orders": {
        "order_id": "PK",
        "customer_id": "FK → customers.customer_id"
    },

    "order_items": {
        "order_item_id": "PK",
        "order_id": "FK → orders.order_id",
        "product_id": "FK → products.product_id"
    },

    "payments": {
        "payment_id": "PK",
        "order_id": "FK → orders.order_id"
    },

    "returns": {
        "return_id": "PK",
        "order_id": "FK → orders.order_id",
        "product_id": "FK → products.product_id"
    },

    "inventory": {
        "inventory_id": "PK",
        "product_id": "FK → products.product_id"
    }
}


# Business descriptions
descriptions = {

    "customer_id": "Unique customer identifier",
    "customer_type": "Customer type, such as B2C or B2B",
    "first_name": "Customer first name",
    "last_name": "Customer last name",
    "email": "Customer email address",
    "postcode_area": "Customer postcode area",
    "city": "Customer city",
    "region": "Customer region",
    "signup_date": "Customer registration date",

    "supplier_id": "Unique supplier identifier",
    "supplier_name": "Supplier name",
    "supplier_country": "Supplier country",
    "supplier_region": "Supplier region",
    "standard_lead_time_days": "Standard supplier lead time in days",
    "payment_terms_days": "Supplier payment terms in days",
    "supplier_status": "Supplier active/inactive status",

    "product_id": "Unique product identifier",
    "product_name": "Product name",
    "category": "Product category",
    "subcategory": "Product subcategory",
    "brand": "Product brand",
    "sourcing_country": "Country where product is sourced",
    "cost_price": "Product purchase cost",
    "selling_price": "Product selling price",
    "reorder_level": "Stock level at which replenishment should be considered",
    "active_flag": "Indicates whether the product is currently active",

    "purchase_order_id": "Unique purchase order identifier",
    "order_date": "Purchase order date",
    "expected_delivery_date": "Expected delivery date",
    "quantity_ordered": "Quantity ordered from supplier",
    "unit_cost": "Purchase cost per unit",
    "purchase_order_status": "Purchase order status",

    "shipment_id": "Unique shipment identifier",
    "origin_country": "Shipment origin country",
    "destination_country": "Shipment destination country",
    "shipment_date": "Shipment dispatch date",
    "estimated_arrival_date": "Estimated shipment arrival date",
    "actual_arrival_date": "Actual shipment arrival date",
    "shipping_method": "Method used to transport shipment",
    "freight_cost": "Shipment freight cost",
    "import_duty": "Import duty cost",
    "other_import_cost": "Other import-related cost",
    "shipment_status": "Shipment status",

    "order_id": "Unique customer order identifier",
    "order_date": "Customer order date/time",
    "order_status": "Customer order status",
    "sales_channel": "Channel through which order was placed",
    "delivery_method": "Customer delivery method",
    "shipping_region": "Customer shipping region",

    "order_item_id": "Unique order line identifier",
    "quantity": "Quantity of product purchased",
    "unit_price": "Selling price per unit at time of order",
    "discount_amount": "Discount applied to order line",

    "payment_id": "Unique payment identifier",
    "payment_date": "Payment date/time",
    "payment_method": "Payment method",
    "payment_status": "Payment status",
    "amount": "Payment amount",

    "return_id": "Unique return identifier",
    "return_date": "Return date",
    "quantity_returned": "Quantity returned",
    "return_reason": "Reason for product return",
    "refund_amount": "Refund amount",
    "return_status": "Return status",

    "inventory_id": "Unique inventory record identifier",
    "inventory_date": "Inventory snapshot date",
    "opening_stock": "Opening inventory quantity",
    "units_received": "Units received during period",
    "units_sold": "Units sold during period",
    "units_returned": "Units returned during period",
    "closing_stock": "Closing inventory quantity"
}


results = []


for table in tables:

    file_path = DATA_DIR / f"{table}.csv"

    if not file_path.exists():
        print(f"WARNING: {file_path} not found")
        continue

    df = pd.read_csv(file_path)

    for column in df.columns:

        results.append({
            "table": table,
            "column": column,
            "data_type": str(df[column].dtype),
            "nullable": df[column].isnull().any(),
            "unique_count": df[column].nunique(),
            "key_role": key_roles.get(table, {}).get(column, ""),
            "business_description": descriptions.get(
                column,
                "Business description to be confirmed"
            )
        })


dictionary = pd.DataFrame(results)


output_file = OUTPUT_DIR / "data_dictionary.csv"

dictionary.to_csv(output_file, index=False)


print("=" * 60)
print("DATA DICTIONARY CREATED")
print("=" * 60)

print("Tables:", dictionary["table"].nunique())
print("Columns:", len(dictionary))
print("Output:", output_file)