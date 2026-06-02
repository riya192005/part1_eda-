# Data Quality Report

## Overview

This report summarizes data quality findings from the customer churn analysis datasets.

---

## Missing Values

### customers.csv

| Column | Missing Values |
|----------|----------|
| loyalty_tier | 1386 |
| skin_type | 401 |

Impact:
- Missing loyalty tier information may affect customer segmentation.
- Missing skin type values may limit personalization analysis.

### orders.csv

| Column | Missing Values |
|----------|----------|
| rating | 80 |

Impact:
- Missing ratings may affect customer satisfaction analysis.

---

## Duplicate Records

### customers.csv

Duplicate rows found: 0

### orders.csv

Duplicate rows found: 0

Impact:
- No duplicate record issues detected.

---

## Date Consistency

The following date columns are stored as text and should be converted to datetime format:

- signup_date
- order_date
- ticket_date
- snapshot_date

Impact:
- Incorrect date formats may affect time-based analysis.

---

## Potential Modeling Leakage

The churn label dataset contains:

- churn_next_60d

This variable must never be used as an input feature when training predictive models.

Future information after the snapshot date should not be included in model features.

---

## Recommendations

1. Convert all date columns to datetime.
2. Investigate missing loyalty_tier values.
3. Investigate missing customer ratings.
4. Monitor support-ticket quality metrics.
5. Apply strict leakage prevention during model development.