# 🛒 E-Commerce Sales & Customer Analytics with SQL and Power BI  

## 📌 Project Overview  
This project demonstrates end-to-end **Sales and Customer Analytics** using **PostgreSQL, Python, and Power BI**.  
The dataset used is the popular **Sample Superstore dataset (Kaggle)**, which was cleaned, transformed, and loaded into PostgreSQL for analytics and visualization.  

The pipeline covers:  
✅ Database schema design  
✅ Data cleaning & splitting with Python (ETL)  
✅ Loading CSV data into PostgreSQL  
✅ SQL analytics queries (sales, profit, customer segmentation)  
✅ Visualization in Power BI  

---

## 🗂️ Project Structure  

ecommerce-sales-analytics/
│
├── sql/
│ ├── schema.sql # Database schema (CREATE TABLE statements)
│ ├── load_data.sql # COPY commands to load CSV data
│ └── analytics_queries.sql # Business analytics SQL queries
│
├── data/
│ ├── Sample - Superstore.csv # Raw dataset
│ ├── customers.csv # Cleaned customers table
│ ├── products.csv # Cleaned products table
│ └── orders.csv # Cleaned orders table
│
├── python/
│ └── split_superstore.py # Python script for data cleaning & splitting
│
├── powerbi/
│ └── ecommerce_dashboard.pbix # Power BI dashboard
│
└── README.md # Project documentation