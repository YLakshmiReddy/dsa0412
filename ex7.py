import pandas as pd

# Sample data
data = {
    'customer_id': [101, 102, 101, 103, 102, 101],
    'order_date': ['2024-01-05', '2024-01-10', '2024-02-15', '2024-03-01', '2024-03-10', '2024-03-15'],
    'product_name': ['Apples', 'Bananas', 'Apples', 'Oranges', 'Bananas', 'Apples'],
    'order_quantity': [5, 3, 2, 4, 6, 1]
}

# Create DataFrame
order_data = pd.DataFrame(data)

# Convert order_date to datetime
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# 1. Total number of orders made by each customer
orders_per_customer = order_data['customer_id'].value_counts().sort_index()

# 2. Average order quantity for each product
avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

# 3. Earliest and latest order dates
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()

# Display results
print("1. Total number of orders by each customer:\n", orders_per_customer)
print("\n2. Average order quantity per product:\n", avg_quantity_per_product)
print(f"\n3. Earliest order date: {earliest_date.date()}")
print(f"   Latest order date: {latest_date.date()}")
