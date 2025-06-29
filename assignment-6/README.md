# 🧠 Assignment 6 – Model Evaluation & Hyperparameter Tuning

> **Internship Task - Celebal Technologies**  
> Completed by: **Devpratap R Singh | Data Science & Analytics Intern**

---

## 📌 Objective

To evaluate the performance of various classification models on the Breast Cancer dataset using key ML evaluation metrics, and improve model performance using:
- 🔍 GridSearchCV (Exhaustive search)
- 🎯 RandomizedSearchCV (Random sampling of parameters)

The goal is to identify the best-performing model using precision, recall, F1-score, and accuracy as evaluation criteria.

---

## 🧪 Dataset

- 📦 **Name:** Breast Cancer Wisconsin Dataset (from `sklearn.datasets`)
- 🧬 **Type:** Binary Classification
- 📈 **Target Labels:** Malignant (0), Benign (1)
- 💡 No missing values, 30 numerical features

---

## 🧠 Models Implemented

| Model                  | Description                           |
|------------------------|---------------------------------------|
| Logistic Regression    | Linear model for binary classification |
| Decision Tree          | Rule-based split learning             |
| Random Forest          | Ensemble of decision trees            |
| SVM                    | Support Vector Classifier             |
| KNN                    | Nearest neighbor voting               |
| Gradient Boosting      | Additive tree-based boosting          |

---

## 📊 Evaluation Metrics Used

Each model was evaluated using:
- ✅ **Accuracy**
- 🎯 **Precision**
- 🔁 **Recall**
- 🧠 **F1-Score**
- 📉 **Confusion Matrix** (visualized)

---

## 🔍 Hyperparameter Tuning Strategy

| Technique            | Applied On             | Notes                            |
|----------------------|------------------------|----------------------------------|
| `GridSearchCV`       | Random Forest          | Exhaustive tuning on grid space |
| `RandomizedSearchCV` | Gradient Boosting      | 10 iterations on parameter dist |

---

## 🏁 Final Results

| Model                    | Accuracy | Precision | Recall | F1-Score |
|--------------------------|----------|-----------|--------|----------|
| Random Forest (Tuned)    | 0.9737   | 0.9761    | 0.9791 | 0.9776   |
| Gradient Boosting (Tuned)| 0.9649   | 0.9615    | 0.9730 | 0.9672   |

> ✅ **Winner:** Tuned Random Forest – highest F1-Score & precision

---

## 🧰 Project Structure

assignment-6/
├── notebooks/
│ └── assignment_6.ipynb # Full notebook with markdown + results
├── scripts/
│ ├── model_training.py # Modular training + evaluation logic
│ ├── hyperparameter_tuning.py # GridSearchCV + RandomizedSearchCV
│ └── evaluate_metrics.py # Confusion matrix + classification report
├── output/
│ ├── confusion_matrices/ # Visuals of confusion matrix
│ ├── baseline_scores.csv # Raw model performance scores
│ └── tuned_scores.csv # Scores after tuning
├── data/
│ └── (empty – used sklearn datasets)
├── requirements.txt # Environment dependencies
└── README.md # This file 📘



---


---

## ✅ Final Instructions:

1. Save the above as `assignment-6/README.md`
2. Commit it:
```bash
git add assignment-6/README.md
git commit -m "🧠 Add polished README for assignment-6"
git push origin main


👨‍💻 Author

Devpratap R Singh
BTech CSE @ Manipal University Jaipur
Data Science & Analytics Intern @ Celebal Technologies
Passionate about AI, ML, and scalable problem-solving 🚀