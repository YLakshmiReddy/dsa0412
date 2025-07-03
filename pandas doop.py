import pandas as pd

df = pd.read_csv('orders.csv')

print("First few rows of the dataset:")
print(df.head())

total_sales = df['Total Price'].sum()
print(f"\nTotal Sales: ₹{total_sales:.2f}")

average_quantity = df['Quantity'].mean()
print(f"\nAverage Quantity Ordered: {average_quantity:.2f}")

top_selling = df.groupby('Product ID')['Quantity'].sum().sort_values(ascending=False)
print("\nTop-Selling Products (based on Quantity):")
print(top_selling.head())
