# Part 3 - Churn Prediction Model

## Objective
Predict customer churn within the next 60 days.

## Files

- churn_model.ipynb
- model.pkl
- metrics.json
- error_analysis.md
- model_card.md
- requirements.txt

## Model

Final Model: Logistic Regression

Performance:

- Accuracy: 81.5%
- Precision: 82.3%
- Recall: 80.4%
- F1 Score: 81.3%
- ROC-AUC: 88.5%

## How To Load

```python
import joblib
model = joblib.load("model.pkl")