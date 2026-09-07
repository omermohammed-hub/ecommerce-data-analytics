import pandas as pd
import random


# --------------------------------------------------
# 1. Supplier configuration
# --------------------------------------------------

supplier_config = {
    "China": {
        "count": 20,
        "regions": [
            "Guangdong",
            "Zhejiang",
            "Jiangsu",
            "Fujian",
            "Shandong"
        ],
        "lead_time_range": (35, 60)
    },

    "India": {
        "count": 12,
        "regions": [
            "Maharashtra",
            "Gujarat",
            "Tamil Nadu",
            "Delhi",
            "Karnataka"
        ],
        "lead_time_range": (20, 40)
    },

    "UK": {
        "count": 8,
        "regions": [
            "England",
            "Scotland",
            "Wales",
            "Northern Ireland"
        ],
        "lead_time_range": (2, 10)
    }
}


# --------------------------------------------------
# 2. Generate suppliers
# --------------------------------------------------

suppliers = []

supplier_number = 1

for country, config in supplier_config.items():

    for _ in range(config["count"]):

        supplier_region = random.choice(config["regions"])

        lead_time = random.randint(
            config["lead_time_range"][0],
            config["lead_time_range"][1]
        )

        payment_terms = random.choice(
            [15, 30, 45, 60]
        )

        supplier_status = random.choices(
            ["Active", "Inactive"],
            weights=[90, 10],
            k=1
        )[0]

        supplier = {
            "supplier_id": f"SUP{supplier_number:05d}",
            "supplier_name": f"{country} Supplier {supplier_number:03d}",
            "supplier_country": country,
            "supplier_region": supplier_region,
            "standard_lead_time_days": lead_time,
            "payment_terms_days": payment_terms,
            "supplier_status": supplier_status
        }

        suppliers.append(supplier)

        supplier_number += 1


# --------------------------------------------------
# 3. Convert to Pandas DataFrame
# --------------------------------------------------

df_suppliers = pd.DataFrame(suppliers)


# --------------------------------------------------
# 4. Save CSV
# --------------------------------------------------

output_path = "data/raw/suppliers.csv"

df_suppliers.to_csv(
    output_path,
    index=False
)


# --------------------------------------------------
# 5. Display results
# --------------------------------------------------

print(f"Created {len(df_suppliers)} suppliers.")
print(f"Saved to: {output_path}")