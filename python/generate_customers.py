import pandas as pd
from faker import Faker
import random
fake = Faker("en_GB")
uk_locations = {
    "Scotland": ["Glasgow", "Edinburgh", "Aberdeen", "Dundee"],
    "North East": ["Newcastle", "Sunderland", "Middlesbrough"],
    "North West": ["Manchester", "Liverpool", "Preston", "Blackpool"],
    "Yorkshire & Humber": ["Leeds", "Sheffield", "York", "Hull"],
    "West Midlands": ["Birmingham", "Coventry", "Wolverhampton"],
    "East Midlands": ["Nottingham", "Leicester", "Derby", "Lincoln"],
    "East of England": ["Cambridge", "Norwich", "Ipswich", "Peterborough"],
    "London": ["London"],
    "South East": ["Southampton", "Brighton", "Reading", "Oxford"],
    "South West": ["Bristol", "Plymouth", "Exeter", "Bournemouth"],
    "Wales": ["Cardiff", "Swansea", "Newport", "Wrexham"],
    "Northern Ireland": ["Belfast", "Derry"]
}
customers = []

for i in range(1, 5001):
    region = random.choice(list(uk_locations.keys()))
    city = random.choice(uk_locations[region])

    customer_type = random.choices(
        ["B2C", "B2B"],
        weights=[85, 15],
        k=1
    )[0]

    customer = {
        "customer_id": f"CUST{i:05d}",
        "customer_type": customer_type,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "postcode_area": fake.postcode().split()[0],
        "city": city,
        "region": region,
        "signup_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    }

    customers.append(customer)
    df_customers = pd.DataFrame(customers)
    
    output_path = "data/raw/customers.csv"

df_customers.to_csv(output_path, index=False)

print(f"Created {len(df_customers)} customers.")
print(f"Saved to: {output_path}")