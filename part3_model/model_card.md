# Churn Prediction Model Card

## Intended Use
Predict customers likely to churn within the next 60 days.

## Data Used
rfm_modeling_snapshot.csv

## Model Approach
Baseline: Logistic Regression
Comparison: Random Forest

## Performance
Accuracy: 81.5%
Precision: 82.3%
Recall: 80.4%
F1 Score: 81.3%
ROC-AUC: 88.5%

## Limitations
- Predictions are based on historical behavior.
- Customer behavior may change over time.
- Model performance may degrade without retraining.

## Ethical Risks
- Customers may be unfairly targeted due to prediction errors.
- False positives may receive unnecessary retention offers.
- False negatives may miss retention opportunities.

## Monitoring Needs
- Track model accuracy monthly.
- Monitor churn rate changes.
- Retrain when performance declines.

## When Not To Use
- For credit decisions.
- For employment decisions.
- As the sole basis for customer treatment.