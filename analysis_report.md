# Sales Data Analysis Report

## 1. Project Overview

This project analyzes a simple sales dataset using Python and Pandas.

### Objectives
- Load and explore the sales data
- Check and clean the dataset
- Handle missing values
- Remove duplicate records
- Calculate important sales metrics
- Identify the best-selling product
- Analyze revenue by region
- Generate business insights

## 2. Dataset Overview

The dataset contains **100 transactions** and **7 columns**.

| Column | Description |
|---|---|
| Date | Date of transaction |
| Product | Product sold |
| Quantity | Number of units sold |
| Price | Product price |
| Customer_ID | Customer identifier |
| Region | Sales region |
| Total_Sales | Total transaction value |

## 3. Data Quality

| Check | Result |
|---|---:|
| Rows | 100 |
| Columns | 7 |
| Missing Values Found | 0 |
| Duplicate Rows Removed | 0 |
| Sales Calculation Mismatches | 0 |

`Total_Sales` was validated against `Quantity × Price`.

## 4. Key Metrics

| Metric | Result |
|---|---:|
| Total Revenue | **₹12,365,048.00** |
| Total Units Sold | **478** |
| Total Transactions | **100** |
| Average Transaction | **₹123,650.48** |
| Average Unit Price | **₹25,808.51** |
| Best-Selling Product | **Laptop** |
| Top Revenue Region | **North** |

## 5. Revenue by Product

| Product | Revenue |
|---|---:|
| Laptop | ₹3,889,210.00 |
| Tablet | ₹2,884,340.00 |
| Phone | ₹2,859,394.00 |
| Headphones | ₹1,384,033.00 |
| Monitor | ₹1,348,071.00 |

**Best-selling product by revenue:** Laptop.

## 6. Units Sold by Product

| Product | Units Sold |
|---|---:|
| Laptop | 136 |
| Tablet | 127 |
| Phone | 101 |
| Monitor | 66 |
| Headphones | 48 |

## 7. Revenue by Region

| Region | Revenue |
|---|---:|
| North | ₹3,983,635.00 |
| South | ₹3,737,852.00 |
| East | ₹2,519,639.00 |
| West | ₹2,123,922.00 |

**Top revenue region:** North.

## 8. Key Insights

1. Total revenue was **₹12,365,048.00**.
2. **Laptop** generated the highest product revenue.
3. **North** generated the highest regional revenue.
4. A total of **478 units** were sold.
5. The analysis covered **100 transactions**.
6. `Total_Sales` had **0** validation mismatches.

## 9. Conclusion

This project demonstrates fundamental data-analysis skills using Pandas:

- Data loading
- Data exploration
- Data cleaning
- Data validation
- Aggregation
- Metric calculation
- Business insight generation

## 10. Running the Project

### Jupyter Notebook

```python
%run sales_analysis.py
```

### Terminal

```bash
pip install -r requirements.txt
python sales_analysis.py
```
