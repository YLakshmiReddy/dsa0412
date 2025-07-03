import math

# Sample data
n = 100
x = 80
p = x / n

# Z for 95% confidence
z = 1.96

# Margin of error
me = z * math.sqrt((p * (1 - p)) / n)

ci_lower = p - me
ci_upper = p + me

print("95% Confidence Interval for proportion:", (ci_lower, ci_upper))
