from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model.pkl")



class Customer(BaseModel):
    
    recency_days: int = 0
    frequency_180d: int = 0
    monetary_180d: float = 0
    return_rate_180d: float = 0
    avg_discount_pct_180d: float = 0
    avg_rating_180d: float = 0
    category_diversity_180d: int = 0
    ticket_count_90d: int = 0
    negative_ticket_rate_90d: float = 0
    avg_resolution_hours_90d: float = 0
    days_since_signup: int = 0
    sessions_30d: int = 0
    product_views_30d: int = 0
    cart_adds_30d: int = 0 
    wishlist_adds_30d: int = 0
    abandoned_carts_30d: int = 0
    email_opens_30d: int = 0
    campaign_clicks_30d: int = 0
    last_visit_days_ago: int = 0

    city_tier_Tier_2: int = 0
    city_tier_Tier_3: int = 0

    age_group_25_34: int = 0
    age_group_35_44: int = 0
    age_group_45_plus: int = 0

    acquisition_channel_Referral: int = 0

    loyalty_tier_Platinum: int = 0
    loyalty_tier_Silver: int = 0

    preferred_category_Fragrance: int = 0

    acquisition_channel_Influencer: int = 0
    acquisition_channel_Instagram: int = 0
    acquisition_channel_Marketplace: int = 0
    acquisition_channel_Organic: int = 0

    preferred_category_Hair_Care: int = 0
    preferred_category_Makeup: int = 0
    preferred_category_Skin_Care: int = 0
    preferred_category_Wellness: int = 0

    marketing_consent_Yes: int = 0

@app.get("/test")
def test():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(customer: Customer):

    

    df = pd.DataFrame([customer.dict()])

    df = df.rename(columns={
        "city_tier_Tier_2": "city_tier_Tier 2",
        "city_tier_Tier_3": "city_tier_Tier 3",
        "age_group_25_34": "age_group_25-34",
        "age_group_35_44": "age_group_35-44",
        "age_group_45_plus": "age_group_45+",
        "preferred_category_Hair_Care": "preferred_category_Hair Care",
        "preferred_category_Skin_Care": "preferred_category_Skin Care"
    })
    df = df[list(model.feature_names_in_)]
    
    

   
    probability = float(model.predict_proba(df)[0][1])
    prediction = int(model.predict(df)[0])

    

    if probability >= 0.7:
         risk = "high"
    elif probability >= 0.4:
         risk = "medium"
    else:
         risk = "low"

    return {
        "churn_probability": round(probability, 3),
        "predicted_class": prediction,
        "risk_level": risk,
        "risk_explanation":
            "Low activity and customer support interactions indicate churn risk.",
    }


@app.post("/batch_predict")
def batch_predict(customers: list[Customer]):

    df = pd.DataFrame([c.dict() for c in customers])

    df = df.rename(columns={
        "city_tier_Tier_2": "city_tier_Tier 2",
        "city_tier_Tier_3": "city_tier_Tier 3",
        "age_group_25_34": "age_group_25-34",
        "age_group_35_44": "age_group_35-44",
        "age_group_45_plus": "age_group_45+",
        "preferred_category_Hair_Care": "preferred_category_Hair Care",
        "preferred_category_Skin_Care": "preferred_category_Skin Care"
    })

    df = df[list(model.feature_names_in_)]

    probs = model.predict_proba(df)[:, 1]
    preds = model.predict(df)

    results = []

    for p, pred in zip(probs, preds):
        results.append({
            "churn_probability": round(float(p), 3),
            "predicted_class": int(pred)
        })

    return {"predictions": results}