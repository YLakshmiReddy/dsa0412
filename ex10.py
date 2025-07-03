import matplotlib.pyplot as plt

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [15000, 18000, 22000, 17000]

# Create line plot
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title("Monthly Sales Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales (in ₹)")
plt.grid(True)
plt.show()

# Create bar plot
plt.bar(months, sales, color='green')
plt.title("Monthly Sales Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales (in ₹)")
plt.show()
