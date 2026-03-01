import pandas as pd
import numpy as np
import random

# Settings
num_rows = 5000
filename = "dirty_inventory.csv"

data = {
    'item_id': [f"A{random.randint(100, 999)}" for _ in range(num_rows)],
    'quantity': [random.choice([random.randint(1, 100), "OUT OF STOCK", "low", None]) for _ in range(num_rows)],
    'price': [random.choice([round(random.uniform(5.0, 500.0), 2), "TBD", "CALL", None]) for _ in range(num_rows)],
    'last_updated': [random.choice(["2023-01-01", "01/05/2023", "2023.05.10", "Pending", None]) for _ in range(num_rows)]
}

df_fake = pd.DataFrame(data)

# Injecting some guaranteed duplicates for your conflict report
for i in range(50):
    df_fake.iloc[i] = df_fake.iloc[i+100]

# Save it
df_fake.to_csv(filename, index=False)
print(f"Success! {filename} generated with {num_rows} rows of messy data.")