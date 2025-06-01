# 🛍️ Customer Purchase Intent Prediction

This project analyzes customer behavior data to predict purchase intent using machine learning models, including Random Forest, Logistic Regression, and Gradient Boosting.

---

## 📁 Project Structure

```
customer-purchase-intent/
├── data/                   # Raw and processed datasets
├── notebooks/              # EDA and modeling notebooks
├── models/                 # Saved models
├── results/                # Model performance metrics and charts
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## 📊 Dataset Overview

The dataset contains customer interaction data and includes features such as:

- Product views
- Session duration
- Cart activity
- Page interaction metrics
- Timestamp-based behavioral features

Target Variable: `Purchase Intent` (classified into 10 segments)

---

## 🧪 Model Performance

Despite testing multiple algorithms, the **Random Forest** classifier yielded the best results, although overall performance was modest.

### 🔍 Classification Report (Random Forest)

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 1     | 0.16      | 0.14   | 0.15     | 22      |
| 2     | 0.07      | 0.05   | 0.06     | 19      |
| 3     | 0.14      | 0.12   | 0.13     | 24      |
| 4     | 0.00      | 0.00   | 0.00     | 18      |
| 5     | 0.18      | 0.14   | 0.16     | 14      |
| 6     | 0.06      | 0.08   | 0.07     | 25      |
| 7     | 0.05      | 0.05   | 0.05     | 22      |
| 8     | 0.13      | 0.17   | 0.15     | 24      |
| 9     | 0.04      | 0.06   | 0.05     | 18      |
| 10    | 0.00      | 0.00   | 0.00     | 14      |

**Overall Metrics:**
- **Accuracy:** 8.5%
- **Macro Average F1-Score:** 0.08
- **Weighted Average F1-Score:** 0.08
- **AUC-ROC:** 0.4789

---

## ⚠️ Observations

- The model struggles with imbalanced class distribution or limited signal in feature variables.
- Many classes (e.g., 4 and 10) are not predicted at all.

---

## 🧠 Recommendations

To improve the model:
- Perform feature engineering and selection
- Apply class balancing techniques (e.g., SMOTE, class weights)
- Explore models like XGBoost or LightGBM
- Tune hyperparameters with GridSearchCV

---

## 🚀 Future Enhancements

- Integrate session-based features
- Implement time-based prediction models
- Deploy as a real-time scoring API using Flask or FastAPI

---

## 👩🏽‍💻 Author

**Cheryl Machingura**  
[GitHub](https://github.com/cheryltaf85) • [LinkedIn](https://www.linkedin.com/in/cherylmachingura)

