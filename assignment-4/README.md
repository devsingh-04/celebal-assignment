# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-green?logo=pandas)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-orange?logo=matplotlib)](https://matplotlib.org/)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()

A deep dive into one of the most iconic datasets in data science history — the Titanic.  
This project showcases advanced **Exploratory Data Analysis (EDA)** techniques using Python and aims to uncover hidden patterns, relationships, and insights that influenced passenger survival.

---

## 📊 Objectives of the EDA

- 🔍 Understand the structure and distribution of the data  
- 🧼 Identify and handle missing values  
- ⚠️ Detect outliers  
- 📈 Visualize key relationships (like gender/class vs survival)  
- 🔁 Interpret correlation between variables  

---

## 🧠 Key Insights

- **Gender** played a significant role in survival — female passengers had a notably higher survival rate.
- **Passenger Class (Pclass)** showed clear distinctions in survival rates — 1st class had the highest.
- **Fare distribution** is heavily right-skewed and contains outliers.
- **Age** showed a normal distribution with a slight skew and missing values.
- Missing values were found in `Age`, `Cabin`, and `Embarked` columns.

---

## 🖼️ Visualizations Included

| Chart | Description |
|-------|-------------|
| 📊 `age_distribution.png` | Histogram showing passenger age distribution |
| 📉 `boxplot_fare.png` | Boxplot highlighting fare outliers |
| 🔥 `correlation_heatmap.png` | Heatmap of Pearson correlation across features |
| 👩‍🚀 `survival_by_gender.png` | Survival distribution by gender |
| 🛳️ `survival_by_class.png` | Survival rates across passenger classes |


---

## 📁 Folder Structure

assignment-4/
├── titanic.csv
├── titanic_eda.py
├── age_distribution.png
├── boxplot_fare.png
├── correlation_heatmap.png
├── survival_by_gender.png
├── survival_by_class.png
└── README.md

---

## 📌 How to Run

> Prerequisites: Python 3.10+, Pandas, Matplotlib, Seaborn  

1. Clone this repo (if not already):

```bash
git clone https://github.com/yourusername/celebal-assignment.git
cd celebal-assignment/assignment-4

Run the EDA script:
python3 titanic_eda.py

