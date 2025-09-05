import pandas as pd

# -----------------------------
# Load the dataset
# -----------------------------
data = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# -----------------------------
# Create Customers table
# -----------------------------
customers = data[[
    "Customer ID", "Customer Name", "Segment", 
    "Country", "City", "State", "Postal Code", "Region"
]]

# Clean + Deduplicate
customers["Customer ID"] = customers["Customer ID"].astype(str).str.strip()
customers = customers.drop_duplicates(subset=["Customer ID"], keep="first")

# Rename for PostgreSQL
customers = customers.rename(columns={
    "Customer ID": "customer_id",
    "Customer Name": "customer_name",
    "Segment": "segment",
    "Country": "country",
    "City": "city",
    "State": "state",
    "Postal Code": "postal_code",
    "Region": "region"
})

customers.to_csv("customers.csv", index=False)

# -----------------------------
# Create Products table
# -----------------------------
products = data[[
    "Product ID", "Category", "Sub-Category", "Product Name"
]]

products["Product ID"] = products["Product ID"].astype(str).str.strip()
products = products.drop_duplicates(subset=["Product ID"], keep="first")

products = products.rename(columns={
    "Product ID": "product_id",
    "Category": "category",
    "Sub-Category": "sub_category",
    "Product Name": "product_name"
})

products.to_csv("products.csv", index=False)

# -----------------------------
# Create Orders table
# -----------------------------
orders = data[[
    "Order ID", "Order Date", "Ship Date", "Ship Mode",
    "Customer ID", "Product ID", "Sales", "Quantity", "Discount", "Profit"
]]

orders = orders.rename(columns={
    "Order ID": "order_id",
    "Order Date": "order_date",
    "Ship Date": "ship_date",
    "Ship Mode": "ship_mode",
    "Customer ID": "customer_id",
    "Product ID": "product_id",
    "Sales": "sales",
    "Quantity": "quantity",
    "Discount": "discount",
    "Profit": "profit"
})

orders.to_csv("orders.csv", index=False)

print("✅ Customers, Products, and Orders CSV files created successfully!")
