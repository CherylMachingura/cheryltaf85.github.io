# 📦 Late Delivery Prediction for E-Commerce Orders

This project leverages machine learning to predict whether an e-commerce order will arrive late, based on shipment and product-related features. The model helps logistics teams take proactive steps to reduce late deliveries and improve customer satisfaction.

---

## 🔍 Problem Statement

In the competitive world of e-commerce, timely delivery is critical to customer retention. Late deliveries can result in poor reviews, cancellations, and customer churn. This project aims to build a predictive model to identify shipments likely to be delayed using historical logistics data.

---

## 📁 Dataset

The dataset was sourced from a simulated shipping log, containing **10,999** order records with the following fields:

- `Warehouse_block`
- `Mode_of_Shipment`
- `Customer_care_calls`
- `Customer_rating`
- `Cost_of_the_Product`
- `Prior_purchases`
- `Product_importance`
- `Gender`
- `Discount_offered`
- `Weight_in_gms`
- `Reached.on.Time_Y.N` (Target)

---

## 🔧 Technologies Used

- **Python** (v3.11)
- **Pandas**, **NumPy** – Data manipulation
- **Scikit-learn** – Model building
- **Matplotlib**, **Seaborn** – Data visualization
- **Plotly Express** – (replaced by Seaborn 2D plots)
- **Jupyter Notebook**

---

## 📊 Workflow

1. **Data Cleaning**
   - Removed duplicates and null values
   - Renamed target column to `Is Late`
   - Encoded categorical features using `LabelEncoder`

2. **Feature Engineering**
   - Selected relevant features excluding ID
   - Split data into training and testing sets (70/30)

3. **Modeling**
   - Trained a `RandomForestClassifier` on the data
   - Evaluated with accuracy, confusion matrix, and classification report

4. **Visualizations**
   - Correlation heatmap of all features
   - Feature importance plot
   - **Pairplot of customer care calls, discount, and weight by delivery status**

---

## 🧠 Results

- The model achieved strong performance in classifying late deliveries.
- Feature importance revealed key predictors such as `Discount_offered`, `Weight_in_gms`, and `Customer_care_calls`.
- 2D visualizations provided clearer, more actionable patterns than 3D scatter plots.

---

## 📈 Sample Visuals

### 🔹 Pairplot of Key Features

This visualization shows the distribution and relationships among customer care calls, discount offered, and product weight, differentiated by whether the delivery was late.

![Pairplot](images/pairplot_late_deliveries.png)

### 🔹 Feature Importance

![Feature Importance](images/feature_importance_sample.png)
