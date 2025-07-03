import pandas as pd

data = [15, 22, 17, 19, 22, 17, 29, 24, 17, 15]
series = pd.Series(data)

# Skewness using pandas
skewness = series.skew()

# Pearson's Median Skewness Coefficient
mean = series.mean()
median = series.median()
std = series.std()
pearson_skew = 3 * (mean - median) / std

print("Skewness (pandas):", skewness)
print("Pearson's Median Skewness Coefficient:", pearson_skew)
