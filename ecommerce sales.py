import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Category': ['Electronics', 'Clothing', 'Home', 'Books', 'Toys', 'Beauty', 'Sports', 'Groceries'],
    'Sales': [150000, 120000, 100000, 80000, 95000, 70000, 110000, 90000]
}

df = pd.DataFrame(data)

df = df.sort_values(by='Sales', ascending=False)

plt.figure(figsize=(8, 4))
sns.lineplot(x='Category', y='Sales', data=df, marker='o')
plt.title("Line Plot - Total Sales by Product Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
sns.scatterplot(x='Category', y='Sales', data=df, s=100)
plt.title("Scatter Plot - Total Sales by Product Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
sns.barplot(x='Category', y='Sales', data=df)
plt.title("Bar Plot - Total Sales by Product Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
