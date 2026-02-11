# Singapore Resale Flat Price Prediction – Project  

## Overview  
This project analyzes Singapore HDB resale flat transactions and builds a machine learning system to predict resale flat prices.  
It follows a complete end-to-end Data Science workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment using FastAPI (backend) and Streamlit (frontend).

---

## Objective  
- Analyze resale transaction patterns  
- Identify key factors influencing flat prices  
- Build and compare multiple regression models  
- Deploy the best-performing model for real-time price prediction  

---

## Dataset  
- Source: Singapore HDB Resale Flat Dataset  
- Type: Structured tabular dataset  
- Target Variable: Resale Price (SGD)  
- Features Include:  
  - Transaction details (year, month)  
  - Location features (town, street name)  
  - Flat characteristics (flat type, flat model, storey range)  
  - Property size (floor area in sqm)  
  - Lease information (remaining lease)  

---

## Tools & Technologies  
- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Joblib  
- FastAPI  
- Uvicorn  
- Streamlit  
- Jupyter Notebook  

---

## Project Workflow  
1. Data loading and understanding  
2. Data cleaning and preprocessing  
3. Feature engineering  
   - Cyclical month encoding (month_sin, month_cos)  
   - Flat age calculation (flat_age = 99 - remaining_lease)  
4. Exploratory Data Analysis (EDA)  
5. Model training using pipelines  
6. Model evaluation and comparison  
7. Best model selection  
8. Backend API development  
9. Frontend integration  

---

## Exploratory Data Analysis (EDA)  

Key insights derived from EDA:  

- Larger floor area significantly increases resale price  
- Certain towns and streets consistently have higher prices  
- Higher storey ranges slightly increase value  
- Lower remaining lease reduces resale price  
- Newer flats (lower flat age) sell at premium prices  

EDA findings directly influenced feature engineering and model selection.

---

## Machine Learning Models  

- Linear Regression  
- HistGradientBoosting Regressor  
- XGBoost Regressor  

All models were trained using consistent preprocessing pipelines.

---

## Model Evaluation  

- Metrics Used:  
  - R² Score  
  - MAE (Mean Absolute Error)  
  - RMSE (Root Mean Squared Error)  

- Best model selected based on high R² and low RMSE  

---

## Backend – FastAPI  

### Backend Structure  

```
backend/
├── main.py
├── best_pipeline.pkl
├── unique_values.pkl
└── requirements.txt
```

### Backend Features  
- Loads trained pipeline (best_pipeline.pkl)  
- Loads categorical unique values  
- Accepts JSON input  
- Performs feature engineering inside API  
- Returns predicted price as JSON response  

### Run Backend  

```
uvicorn main:app --reload
```

---

## Frontend – Streamlit  

### Frontend Structure  

```
frontend/
├── app.py
├── unique_values.pkl
└── requirements.txt
```

### Frontend Features  
- Dropdown inputs for categorical features  
- Sliders for numeric features  
- Sends POST request to FastAPI backend  
- Displays formatted resale price in SGD  

### Run Frontend  

```
streamlit run app.py
```

---

## Full Repository Structure  

```
Resale-Flat-Price-Prediction/
│
├── backend/
│   ├── main.py
│   ├── best_pipeline.pkl
│   ├── unique_values.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── unique_values.pkl
│   └── requirements.txt
│
├── eda_resale_analysis.ipynb
├── model_training.ipynb
└── README.md
```

---

## Deployment  

- Backend deployed using Render  
- Frontend deployed using Streamlit Cloud  
- Frontend communicates with backend via REST API  

---

## Author  
JK11
