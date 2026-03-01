# Import Libraries 

import pandas as pd
import matplotlib.pyplot as plt

# Load Data
source_file = 'dirty_inventory.csv'
df = pd.read_csv(source_file)

# Data Audit 
invalid_prices = pd.to_numeric(df['price'], errors='coerce').isnull().sum()
missing_ids = df['item_id'].isnull().sum()
duplicates = df.duplicated(subset=['item_id']).sum()    
invalid_count = pd.to_numeric(df['quantity'], errors='coerce').isnull().sum()

# Date Audit
strict_dates = pd.to_datetime(df['last_updated'], format='%Y-%m-%d', errors='coerce')
misformatted_dates = strict_dates.isnull().sum()
invalid_dates = df['last_updated'].isnull().sum()

# Create conflict list for the CSV (All columns)
duplicate_mask = df.duplicated(subset=['item_id'], keep=False)
full_conflict_report = df[duplicate_mask].sort_values(by='item_id')

# Create summary for the terminal (Short list)
id_counts = df['item_id'].value_counts()
duplicate_summary = id_counts[id_counts > 1]

# 3. REPORTING
print(f"\n ----- AI Readiness Report For: {source_file} -----")
print(f"- Missing IDs: {missing_ids}")
print(f"- Duplicate IDs (Total Rows): {duplicates}")
print(f"- Non-Numeric Prices: {invalid_prices}")
print(f"- Quantity Issues: {invalid_count}")

print("\n--- DUPLICATE ID CONFLICT SUMMARY ---")
if duplicate_summary.empty:
    pass
else:
    print(duplicate_summary.head(20)) 
    print(f"\nTotal unique IDs with conflicts: {len(duplicate_summary)}")
    print('--> Check "action_required_duplicates.csv" for full row details.')

# 4. CLEANING
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0)
df['last_updated'] = pd.to_datetime(df['last_updated'], errors='coerce')

# 5. EXPORT
df.to_csv("cleaned_inventory_v1.csv", index=False)
full_conflict_report.to_csv("action_required_duplicates.csv", index=False)

print("\n--- EXPORT COMPLETE ---")
print("1. 'cleaned_inventory_v1.csv' (Standardized Data)")
print("2. 'action_required_duplicates.csv' (Full Conflict Details)")

# 6. VISUALIZE
errors = {'NaN Prices': invalid_prices, 'Missing IDs': missing_ids, 'Duplicate IDs': duplicates, 'NaN Qty': invalid_count}
plt.bar(errors.keys(), errors.values(), color='skyblue')
plt.title(f'Data Quality Audit: {source_file}')
plt.ylabel('Error Count')
plt.show()

print('Hello World')