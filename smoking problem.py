import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Smoking': [20, 15, 5, 25, 30, 10, 18, 22, 8, 12],
    'LungCancer': [5, 4, 1, 6, 8, 2, 3, 7, 1, 2]
}

df = pd.DataFrame(data)

correlation = df['Smoking'].corr(df['LungCancer'])
print(f"Correlation Coefficient between Smoking and Lung Cancer: {correlation:.2f}")

sns.scatterplot(x='Smoking', y='LungCancer', data=df)
plt.title('Scatter Plot: Smoking vs Lung Cancer')
plt.xlabel('Smoking (Cigarettes/Level)')
plt.ylabel('Lung Cancer (Index)')
plt.grid(True)
plt.show()
