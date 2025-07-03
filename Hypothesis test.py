import scipy.stats as stats
import math

# Sample stats
mean_A, std_A, n_A = 6.2, 1.5, 100
mean_B, std_B, n_B = 5.8, 1.2, 120

# Z-test
se = math.sqrt((std_A**2)/n_A + (std_B**2)/n_B)
z = (mean_A - mean_B) / se

# p-value for two-tailed test
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

alpha = 0.05
print("Z-statistic:", z)
print("P-value:", p_value)
print("Significant difference?" , "Yes" if p_value < alpha else "No")
