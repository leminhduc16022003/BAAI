#
# Finn;2025/10/22
# Apply correlation analysis to business problems
#
import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
# 1. Input
df= pd.read_csv('Correlataion_Analysis_Data.csv')
# print(df.iloc[:,1:6])

df.info()

# correclation, pvalue = stats.pearsonr(df['Marketing_Spend'],df['Sales_Revenue'])
# 2. Process
correlation_matrix = df.iloc[:,1:6].corr()
print(correlation_matrix.round(3))


# print(df.isnull().sum())
# print(df.isnull().sum().sum())
# 3. Output
# print("Data loaded succesfully!")
# print(f"Dataset shape: {df.shape}")
# correclation, pvalue = stats.pearsonr(df['Marketing_Spend'],df['Sales_Revenue'])
# print(f'Correlation: {correclation: .2f}')
# print(f'P value: {pvalue: .4e}')
print(sns.heatmap (correlation_matrix))
plt.title('Finn is the most intelligent person in the world')
plt.tight_layout()
plt.show()