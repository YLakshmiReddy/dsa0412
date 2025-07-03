import numpy as np

# Sample 3x3 matrix: prices for 3 products over 3 transactions/weeks/days
sales_data = np.array([
    [100, 150, 200],   # Product 1
    [80,  120, 160],   # Product 2
    [90,  110, 130]    # Product 3
])

# 1. Calculate the average price of all products sold
average_price = np.mean(sales_data)

# 2. Print the result
print(f"Average price of all products sold in the past month: ₹{average_price:.2f}")
