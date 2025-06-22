# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# load the dataset 
df = pd.read_csv("netflix_titles.csv")

# Quick look at the dataset 
print(df.head())
print(df.info())
print(df.isnull().sum())

# cleaning the dataset 
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
df.dropna(subset=['country', 'rating', 'date_added'], inplace=True)

# here we will check the content type for eg Movies v/s TV Shows 
plt.figure(figsize=(6,6))
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Content Type Distribution')
plt.show()

# Top 10 countries with most content
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='rocket')
plt.title('Top 10 Countries by Number of Titles')
plt.xlabel('Count')
plt.show()

# year wise content addition
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='year_added', hue='type', palette='muted')
plt.title('Content Added Per Year by Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Most popular ratings
# most common genres 
df['listed_in'] = df['listed_in'].str.split(', ')
genres = df.explode('listed_in')
top_genres = genres['listed_in'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='coolwarm')
plt.title('Top 10 Genres')
plt.xlabel('Number of Titles')
plt.show()
plt.savefig("plot_name.png")  # Save any plot like this
