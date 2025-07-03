import numpy as np
from scipy import stats

# Example Data
sample_data = [22, 25, 24, 20, 23, 21, 22, 23, 26, 24]  # sample
population_mean = 24  # assumed population mean (for H0)

# 🎯 One-sample t-test (is sample mean significantly different from population mean?)
t_stat, p_value = stats.ttest_1samp(sample_data, population_mean)

print("One-sample t-test")
print("T-statistic:", t_stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Reject the null hypothesis (significant difference).")
else:
    print("Fail to reject the null hypothesis (no significant difference).")

# ----------------------------------------------

# 🧪 Two-sample t-test (independent)
group1 = [22, 23, 21, 24, 25]
group2 = [26, 28, 27, 30, 29]

t_stat, p_value = stats.ttest_ind(group1, group2)

print("\nTwo-sample t-test")
print("T-statistic:", t_stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Reject the null hypothesis (groups are significantly different).")
else:
    print("Fail to reject the null hypothesis (no significant difference).")