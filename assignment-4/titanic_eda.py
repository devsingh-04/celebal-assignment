# titanic_eda.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')



# First Look
print("First 5 rows:\n", df.head())
print("\nShape of dataset:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# Summary Stats
print("\nSummary Statistics:\n", df.describe(include='all'))

# Visualizations - Distributions
sns.histplot(df['Age'].dropna(), kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.savefig("age_distribution.png")
plt.clf()

sns.boxplot(x='Pclass', y='Age', data=df)
plt.title("Age vs Passenger Class")
plt.savefig("age_vs_pclass.png")
plt.clf()

# Heatmap for Missing Data
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.savefig("missing_values_heatmap.png")
plt.clf()

# Correlation Heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.clf()

# Relationship between features and survival
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title("Survival by Gender")
plt.savefig("survival_by_gender.png")
plt.clf()

sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title("Survival by Passenger Class")
plt.savefig("survival_by_class.png")
plt.clf()

print("\nEDA complete. Charts saved as PNG files.")
