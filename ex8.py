import pandas as pd

# Sample sales data
sales_data = pd.DataFrame({
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Mouse', 'Tablet', 'Phone', 'Laptop', 'Mouse'],
    'quantity_sold': [3, 5, 2, 4, 6, 8, 3, 7, 1, 2]
})

# Group by product and sum quantities
top_products = sales_data.groupby('product_name')['quantity_sold'].sum()

# Sort and get top 5
top_5 = top_products.sort_values(ascending=False).head(5)

print("Top 5 most sold products:")
print(top_5)
