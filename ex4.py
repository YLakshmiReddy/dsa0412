import numpy as np

# Quarterly sales data (in ₹)
sales_data = np.array([150000, 175000, 200000, 250000])  # Q1 to Q4

# 1. Total sales for the year
total_sales = np.sum(sales_data)

# 2. Percentage increase from Q1 to Q4
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

# 3. Print results
print(f"Total sales for the year: ₹{total_sales}")
print(f"Percentage increase from Q1 to Q4: {percentage_increase:.2f}%")
