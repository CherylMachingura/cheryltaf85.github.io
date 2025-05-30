# Customer Churn Prediction

## Objective
Build predictive models to determine whether a credit card customer is likely to churn, based on account activity and customer behavior.

## Dataset
- Source: BankChurners.csv (Kaggle)
- Includes attributes such as customer age, credit limit, card category, and transaction data

## Methods
- Data preprocessing: missing value handling, label encoding, scaling
- Model development: Logistic Regression, K-Nearest Neighbors (KNN), Random Forest
- Model evaluation using Accuracy, Precision, Recall, F1-Score, and ROC AUC
- Feature importance analysis to identify top drivers of churn

## Tools & Libraries
Python, pandas, scikit-learn, matplotlib, seaborn

## Key Insights
- Random Forest performed best with high recall and precision
- Transaction counts, total relationship count, and credit utilization were key indicators of churn
- Visualizations helped validate class imbalance and model reliability

## Ethical Considerations
- Care taken to avoid bias in model training and data interpretation
- Protected features (e.g., age) were monitored to ensure fairness
