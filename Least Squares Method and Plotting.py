import numpy as np
import matplotlib.pyplot as plt

x = np.array([8, 3, 2, 10, 11, 3, 6, 5, 6, 8])
y = np.array([4, 12, 1, 12, 9, 4, 6, 1, 6, 14])

# Least squares fit (y = mx + c)
m, c = np.polyfit(x, y, 1)

# Predicted values
y_pred = m * x + c

# Plot
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label=f'Best Fit Line: y = {m:.2f}x + {c:.2f}')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Least Squares Line Fit")
plt.grid(True)
plt.show()
