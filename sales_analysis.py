"""
Sales Data Analysis - Beginner Pandas Project

Run in Jupyter:
    %run sales_analysis.py

Run in terminal:
    python sales_analysis.py
"""

from pathlib import Path
import pandas as pd

# Find the CSV file in the same folder as this script.
BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "sales_data.csv")

# Explore the dataset.
print("Rows and columns:", df.shape)
print("Columns:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Clean the data.
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

for column in df.select_dtypes(include="number").columns:
    df[column] = df[column].fillna(df[column].median())

for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].fillna("Unknown")

df = df.drop_duplicates()

# Validate Total_Sales using Quantity x Price.
df["Calculated_Sales"] = df["Quantity"] * df["Price"]
mismatches = (
    df["Total_Sales"].round(2) != df["Calculated_Sales"].round(2)
).sum()

# Calculate key metrics.
total_revenue = df["Total_Sales"].sum()
total_units = df["Quantity"].sum()
total_transactions = len(df)
average_transaction = df["Total_Sales"].mean()
average_price = df["Price"].mean()

product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

product_units = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

region_sales = (
    df.groupby("Region")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

best_product = product_sales.index[0]
top_region = region_sales.index[0]

# Display a clean report.
print("\n" + "=" * 55)
print("              SALES DATA ANALYSIS")
print("=" * 55)
print(f"Total Revenue        : ₹{total_revenue:,.2f}")
print(f"Total Units Sold     : {total_units:,}")
print(f"Transactions         : {total_transactions:,}")
print(f"Average Transaction  : ₹{average_transaction:,.2f}")
print(f"Average Unit Price   : ₹{average_price:,.2f}")
print(f"Best-Selling Product : {best_product}")
print(f"Top Revenue Region   : {top_region}")
print(f"Sales Validation Errors: {mismatches}")

print("\nRevenue by Product:")
print(product_sales)

print("\nUnits Sold by Product:")
print(product_units)

print("\nRevenue by Region:")
print(region_sales)

# Save useful output files.
df.to_csv(BASE_DIR / "cleaned_sales_data.csv", index=False)
product_sales.to_csv(BASE_DIR / "product_sales_summary.csv", header=["Total_Sales"])
region_sales.to_csv(BASE_DIR / "region_sales_summary.csv", header=["Total_Sales"])

print("\nAnalysis completed successfully.")
