# Developer-Salary-Prediction
# 💼 Developer Salary Prediction Model

A machine learning pipeline that predicts developer salaries based on Stack Overflow survey data. Built with XGBoost and scikit-learn, with a Flask API for deployment.

```

---

## ⚙️ Features Used

| Feature | Description |
|---|---|
| `Country` | Developer's country (top 15 + "Other") |
| `YearsCode` | Years of coding experience (numeric) |
| `EdLevel` | Highest education level |
| `Employment` | Employment type (Full-time, Freelance, etc.) |
| `LanguageHaveWorkedWith` | Number of languages worked with |

**Target:** `ConvertedCompYearly` — annual salary in USD (filtered between $10,000 and $500,000)

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- `scikit-learn`
- `xgboost`
- `pandas`
- `numpy`
- `matplotlib`
- `joblib`
- `flask`

### 2. Add the Data

Download the Stack Overflow Developer Survey dataset and place the CSV at:

```
Data/Raw/developer-survey-2025.csv
```

### 3. Train the Model

```bash
python train.py
```

This will:
- Load and clean the raw survey data
- Split into training and test sets (80/20)
- Train an XGBoost regression model inside a scikit-learn pipeline
- Print evaluation metrics (MAE, RMSE, R²)
- Save a predictions plot to `Data/predictions_plot.png`
- Save the trained pipeline to `models/salary_pipeline.pkl`

---

## 🧪 Model Details

### Preprocessing Pipeline

**Numeric features** (`YearsCode`, `LanguageHaveWorkedWith`):
1. Median imputation for missing values
2. Standard scaling

**Categorical features** (`Country`, `EdLevel`, `Employment`):
1. Most-frequent imputation for missing values
2. One-Hot Encoding (`drop='first'`, unknown categories → zeros)

### Model

XGBoost Regressor with the following configuration:

```python
{
    'n_estimators': 300,
    'max_depth': 5,
    'learning_rate': 0.05,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'tree_method': 'hist'   # Fast histogram-based training
}
```

---

## 📊 Evaluation

The model is evaluated on the held-out test set using:

- **MAE** — Mean Absolute Error (average $ prediction error)
- **RMSE** — Root Mean Squared Error
- **R²** — Coefficient of Determination (variance explained)

Two plots are generated:
- **Actual vs. Predicted Salary** — scatter plot against the perfect prediction line
- **Residual Distribution** — histogram of prediction errors

---

## 🌐 API (Flask — In Progress)

A REST API is being built using Flask to serve predictions.

**Planned endpoint:**

```
POST /predict
```

**Request body:**
```json
{
  "Country": "United States of America",
  "YearsCode": 8,
  "EdLevel": "Bachelor's",
  "Employment": "Full-time",
  "LanguageHaveWorkedWith": 5
}
```

**Response:**
```json
{
  "predicted_salary": 112500,
  "margin_of_error": 18400
}
```

> ⚠️ The Flask API (`app.py`) is currently under development and not yet production-ready.

---

## 📌 Known Issues & TODOs

- [ ] Complete Flask API (`app.py`)
- [ ] Handle `"Less than 1 year"` and `"More than 50 years"` text values in `YearsCode`
- [ ] Add cross-validation to training script
- [ ] Containerize with Docker for deployment

---

## 📄 Data Source

[Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

