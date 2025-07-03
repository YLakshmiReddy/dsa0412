import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('orders.csv')  # Replace with your dataset filename

import numpy as np
df['OrderID'] = df['Order ID'].astype(str)
df['Order Date'] = pd.to_datetime(
    np.random.choice(pd.date_range("2024-01-01", "2024-12-31"), size=len(df))
)

customer_id = 'C045'  # Replace with any actual CustomerID from your data
filtered_df = df[df['Customer ID'] == customer_id]
print(f"\nOrders for customer {customer_id}:\n", filtered_df)

total_spent = df.groupby('Customer ID')['Total Price'].sum().reset_index()
print("\nTotal Amount Spent by Each Customer:\n", total_spent)

plt.figure(figsize=(8, 5))
sns.histplot(df['Total Price'], bins=30, kde=True)
plt.title("Histogram of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
