import pandas as pd
import os

# ✅ Create 'data' folder INSIDE your project
os.makedirs("data", exist_ok=True)

# ✅ Sample data
data1 = pd.DataFrame({
    "Product": ["Widget A", "Widget B", "Widget C"],
    "Sales": [120, 200, 150],
    "Date": ["2025-01-05", "2025-01-08", "2025-01-12"]
})

data2 = pd.DataFrame({
    "Product": ["Widget A", "Widget B", "Widget D"],
    "Sales": [100, 250, 50],
    "Date": ["2025-02-04", "2025-02-10", "2025-02-11"]
})

# ✅ Save inside current project folder
data1.to_excel("data/sales_jan.xlsx", index=False)
data2.to_excel("data/sales_feb.xlsx", index=False)

print("✅ Sample Excel files created in the 'data' folder.")

