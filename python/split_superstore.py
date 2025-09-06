import pandas as pd
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Load Superstore dataset
data = pd.read_csv(os.path.join(DATA_DIR, "Sample - Superstore.csv"), encoding="latin1")

# -------------------
# Split into customers
# -------------------
customers = data[[
    "Customer ID", "Customer Name", "Segment",
    "Country", "City", "State", "Postal Code", "Region"
]].drop_duplicates()

# -------------------
# Split into products
# -------------------
products = data[[
    "Product ID", "Category", "Sub-Category", "Product Name"
]].drop_duplicates()

# -------------------
# Split into orders
# -------------------
orders = data[[
    "Order ID", "Order Date", "Ship Date", "Ship Mode",
    "Customer ID", "Product ID", "Sales", "Quantity", "Discount", "Profit"
]]

# Save to data/ folder
customers.to_csv(os.path.join(DATA_DIR, "customers.csv"), index=False)
products.to_csv(os.path.join(DATA_DIR, "products.csv"), index=False)
orders.to_csv(os.path.join(DATA_DIR, "orders.csv"), index=False)

print("✅ Split completed! customers.csv, products.csv, orders.csv saved in data/")
