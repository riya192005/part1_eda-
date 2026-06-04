# Error Analysis

## Overview

The final Logistic Regression model achieved:

- Accuracy: 0.815
- Precision: 0.823
- Recall: 0.804
- F1 Score: 0.813
- ROC-AUC: 0.885

During evaluation:

- False Positives: 29
- False Negatives: 33

---

## False Positive Analysis

False Positives are customers predicted to churn who ultimately did not churn.

Business Impact:

- Retention offers may be sent unnecessarily.
- Marketing budget may be wasted on customers who would have stayed anyway.
- However, this error is generally less costly than missing a customer who is actually going to churn.

Example Customers:

1. CUST00016
2. CUST00018
3. CUST00024
4. CUST00025
5. CUST00030

Observed Patterns:

- High inactivity periods.
- Multiple support interactions.
- Reduced engagement signals.
- Churn-like behavior despite remaining active.

---
---

## False Negative Analysis

False Negatives are customers who actually churned but were predicted to stay.

Business Impact:

- Lost customers are not targeted for retention campaigns.
- Potential revenue is lost because intervention happens too late.
- This is generally the more costly error because churned customers may never return.

Example Customers:

1. CUST00088
2. CUST00184
3. CUST00247
4. CUST00379
5. CUST00442

Observed Patterns:

- These customers appeared relatively healthy before the churn event.
- Their purchase and engagement behavior may not have shown strong warning signs.
- Some customers may have reduced activity suddenly, making prediction difficult.

## False Negative Analysis

False Negatives are customers predicted to stay who actually churned.

Business Impact:

- Lost opportunity for intervention.
- Revenue loss.
- Reduced customer lifetime value.
- Potential damage to long-term retention goals.

Example Customers:

1. Customer Example FN-1
2. Customer Example FN-2
3. Customer Example FN-3
4. Customer Example FN-4
5. Customer Example FN-5

Observed Patterns:

- Some customers maintained moderate activity levels before churn.
- Certain churn signals may not be fully captured by available features.
- Sudden behavioral changes may occur after the snapshot date.

---

## Key Findings

The model captures most churn behavior successfully but struggles with customers whose behavior lies near the decision boundary.

Future improvements may include:

- More behavioral features.
- Time-series activity trends.
- Campaign response history.
- Product-level engagement metrics.
---

## False Negative Analysis

False Negatives are customers who actually churned but were predicted to stay.

Business Impact:

- Lost customers are not targeted with retention campaigns.
- Revenue loss may occur due to missed intervention opportunities.
- This is generally the more costly error type because churned customers may never return.

Example Customers:

1. CUSTOMER_ID_1
2. CUSTOMER_ID_2
3. CUSTOMER_ID_3
4. CUSTOMER_ID_4
5. CUSTOMER_ID_5

Observed Patterns:

- Moderate purchase activity before churn.
- Fewer warning signals than typical churn customers.
- Some customers may have changed behavior suddenly.
---

## Conclusion

The Logistic Regression model achieved strong performance with an ROC-AUC of 0.885.

Most errors occurred for customers whose behavior was borderline between active and churn-risk profiles.

From a business perspective, accepting some false positives is preferable to missing high-value customers who are likely to churn.
---

## Conclusion

The Logistic Regression model achieved:

- Accuracy: 81.5%
- Precision: 82.3%
- Recall: 80.4%
- F1 Score: 81.3%
- ROC-AUC: 88.5%

The model demonstrates strong ability to identify customers likely to churn. False positives create additional retention costs, while false negatives represent missed opportunities to save valuable customers. From a business perspective, minimizing false negatives is especially important because customer churn directly impacts revenue and long-term customer value.