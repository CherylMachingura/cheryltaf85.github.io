
# 🛡️ Fraud Detection in Credit Card Transactions

## 📌 Project Overview
This project focuses on identifying fraudulent credit card transactions using advanced machine learning techniques. As financial fraud becomes increasingly sophisticated, building an accurate and scalable detection system is critical for financial institutions to mitigate losses and protect customers.

This work explores both supervised and unsupervised approaches for fraud detection, including techniques such as **Random Forest**, **Logistic Regression**, and **Isolation Forest**, applied to highly imbalanced transaction data.

## 🎯 Objectives
- Detect fraudulent transactions from historical data
- Address extreme class imbalance
- Evaluate the effectiveness of various machine learning models
- Minimize false positives while maintaining high recall for fraud cases

## 📁 Project Structure
```
fraud-detection/
│
├── data/                       # Raw and processed datasets
│   └── creditcard.csv
│
├── notebooks/                 # Jupyter Notebooks for EDA and modeling
│   ├── 01_EDA.ipynb
│   ├── 02_Model_Baseline.ipynb
│   ├── 03_Advanced_Modeling.ipynb
│
├── models/                    # Saved models and evaluation results
│
├── utils/                     # Helper functions for preprocessing, metrics, etc.
│   └── preprocessing.py
│
├── outputs/                   # Final plots and reports
│   ├── confusion_matrix.png
│   └── classification_report.txt
│
├── README.md
└── requirements.txt
```

## 🧠 Methodology
### 🧹 Data Preprocessing
- Handled extreme class imbalance using SMOTE and under-sampling
- Scaled features using MinMaxScaler
- Removed irrelevant columns (e.g., time stamps)

### 📊 Exploratory Data Analysis
- Analyzed transaction amounts, fraud distribution, feature correlations
- Visualized class imbalance and outliers

### ⚙️ Models Applied
- **Logistic Regression**: Baseline classifier
- **Random Forest Classifier**: Ensemble method for interpretability and performance
- **Isolation Forest**: Unsupervised anomaly detection
- **XGBoost**: Gradient boosting for improved recall
- **AutoEncoder** (Optional): Deep learning-based anomaly detection

### 🧪 Evaluation Metrics
- Precision, Recall, F1-score
- Confusion Matrix
- ROC-AUC Curve
- Cost of false positives vs false negatives

## 📈 Results Summary
| Model              | Precision | Recall | F1-Score | AUC-ROC |
|-------------------|-----------|--------|----------|---------|
| Logistic Regression | 0.78      | 0.62   | 0.69     | 0.89    |
| Random Forest       | 0.90      | 0.74   | 0.81     | 0.95    |
| Isolation Forest    | 0.30      | 0.76   | 0.43     | 0.60    |
| XGBoost             | 0.92      | 0.79   | 0.85     | 0.96    |

> ✅ Final selected model: **XGBoost** due to its high recall and AUC.

## 📉 Visualizations
- Fraud vs non-fraud distribution
- Feature importance (tree-based models)
- ROC Curves for model comparison
- Confusion Matrix Heatmaps

## 🧭 Ethical Considerations
- Ensured model fairness: sensitive attributes like gender or geography were excluded
- Addressed class imbalance to avoid bias toward majority class
- Discussed implications of false positives vs false negatives in real-world settings

## 🛠 Tech Stack
- Python (pandas, scikit-learn, imbalanced-learn, xgboost)
- Jupyter Notebook
- Matplotlib / Seaborn for visualization

## 🔍 Future Work
- Integrate real-time fraud detection pipeline with stream processing (e.g., Kafka, Spark)
- Deploy model via Flask or FastAPI for API-based detection
- Enhance detection using LSTM or deep autoencoders on transaction sequences

## 📚 References
- [Credit Card Fraud Detection Dataset – Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Dal Pozzolo, A., Boracchi, G., Caelen, O., Alippi, C., & Bontempi, G. (2017). Credit card fraud detection: a realistic modeling and a novel learning strategy. *IEEE transactions on neural networks and learning systems*, 29(8), 3784–3797.

## 👩‍💻 Author
**Cheryl Machingura**  
Principal Program Manager | Aspiring Data Scientist  
[LinkedIn](https://www.linkedin.com/in/cherylmachingura/) | [GitHub](https://github.com/cheryltaf85/Data-Science-projects) | [Email](mailto:cheryl.machingura@discover.com)
