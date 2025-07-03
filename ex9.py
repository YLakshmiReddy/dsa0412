import pandas as pd

# Sample data
property_data = pd.DataFrame({
    'property_id': [101, 102, 103, 104, 105],
    'location': ['Chennai', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai'],
    'bedrooms': [3, 5, 2, 4, 6],
    'area_sqft': [1500, 2200, 1100, 1800, 2500],
    'listing_price': [5000000, 8500000, 4200000, 6000000, 9000000]
})

# 1. Average listing price per location
avg_price_by_location = property_data.groupby('location')['listing_price'].mean()

# 2. Number of properties with more than 4 bedrooms
count_large_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]

# 3. Property with the largest area
largest_area_property = property_data.loc[property_data['area_sqft'].idxmax()]

print("1. Average price by location:\n", avg_price_by_location)
print("\n2. Properties with more than 4 bedrooms:", count_large_bedrooms)
print("\n3. Property with largest area:\n", largest_area_property)
