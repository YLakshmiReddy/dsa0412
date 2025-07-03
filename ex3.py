import numpy as np

# Sample house data: [bedrooms, square footage, sale price]
house_data = np.array([
    [3, 1800, 350000],
    [5, 2500, 550000],
    [4, 2000, 400000],
    [6, 3000, 750000],
    [2, 1600, 300000]
])

# 1. Filter houses with more than 4 bedrooms
houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]

# 2. Extract sale prices (column index 2)
sale_prices = houses_with_more_than_4_bedrooms[:, 2]

# 3. Calculate average sale price
average_price = np.mean(sale_prices)

# 4. Print result
print(f"Average sale price of houses with more than 4 bedrooms: ₹{average_price:.2f}")
