# 🏠 House Price Prediction — Data Preprocessing & Feature Engineering

This project is part of my **Celebal Technologies Internship Assignment-5**, focused on advanced data preprocessing and feature engineering for a supervised machine learning regression task.

The goal is to build a predictive model to estimate the sale prices of houses using the Ames Housing dataset provided by Kaggle.

---

## 📂 Folder Structure

assignment-5/
├── data/ # Contains train.csv and test.csv
├── house_price_prediction.ipynb # Main Jupyter notebook with full pipeline
├── house_price_predictions.csv # Final submission predictions
└── README.md # This file


---

## 📊 Dataset

- Source: [Kaggle House Prices Competition](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
- Train rows: 1,460
- Test rows: 1,459
- Features: 80 explanatory variables (numeric, categorical)

---

## 🔧 Workflow Summary

### ✅ Step-by-step Pipeline:
- Data Loading and Exploratory Data Analysis (EDA)
- Smart Missing Value Imputation (based on context: "None", median, mode)
- Manual Feature Engineering:
  - `TotalSF`, `AgeOfHouse`, `WasRemodeled`, `TotalBathrooms`, `TotalPorchSF`
- Label simplification for quality features
- One-Hot Encoding of categorical variables
- Feature Scaling using `StandardScaler`
- Model training with Linear Regression, Random Forest, and XGBoost
- XGBoost performed best and used for final predictions

---

## 📈 Results

| Model               | RMSE (Validation) |
|---------------------|-------------------|
| Linear Regression   | ~XX.XX            |
| Random Forest       | ~XX.XX            |
| XGBoost             | ✅ Best (~XX.XX)   |

---

## 🧠 Tech Stack

- Python 3.x
- Jupyter Notebook
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost

---

## 🚀 Outcome

Generated final predictions for unseen test data and saved as `house_price_predictions.csv`.

This assignment demonstrates industry-grade data science workflow and model building using real-world datasets.

---

## 👨‍💻 Author

**Dev Singh**  
B.Tech CSE | Manipal University Jaipur  
Data Science Intern @ Celebal Technologies  
