import numpy as np

# Fuel efficiency data in miles per gallon (mpg)
fuel_efficiency = np.array([22, 25, 28, 32, 36])  # Example: 5 car models

# 1. Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# 2. Choose two models, e.g., model 1 and model 5
model1_eff = fuel_efficiency[0]  # first model
model5_eff = fuel_efficiency[4]  # fifth model

# 3. Calculate percentage improvement from model 1 to model 5
percentage_improvement = ((model5_eff - model1_eff) / model1_eff) * 100

# 4. Print results
print(f"Average fuel efficiency: {average_efficiency:.2f} mpg")
print(f"Percentage improvement from model 1 to model 5: {percentage_improvement:.2f}%")
