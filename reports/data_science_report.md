# Data Science Challenges Report

## 1. Problem Definition
### Problem
Predict the nightly price of an Airbnb listing using property attributes, location, host information, and reviews.

### Target Variable
`price_clean`

### Success Metrics
* MAE — Average absolute prediction error in dollars
* RMSE — Penalizes larger prediction mistakes
* MAPE — Percentage-based error interpretation

## 2. Feature Engineering

## 3. Model Selection

## 4. Validation Strategy

## 5. Model Comparison

## 6. Residual Analysis
Residual analysis reveals whether the model systematically underestimates luxury properties or overestimates low-cost listings.

## 7. Explainability

## 8. Demand Forecasting
Lower availability may indicate higher demand periods, allowing hosts to apply dynamic pricing strategies.

## 9. Listing Segmentation
Example:
* Cluster 0 → Budget listings with low capacity.
* Cluster 1 → Premium large properties.
* Cluster 2 → Highly reviewed popular listings.
* Cluster 3 → Moderate-priced family accommodations.

## 10. Model Generalization
Higher errors in certain neighbourhoods indicate that the model does not generalize equally across geographic regions.

## 11. Bias and Fairness Analysis
### Potential Sources of Bias

- Expensive neighbourhoods are overrepresented.
- Review scores may favor established hosts.
- New listings have limited historical information.

### Mitigation Strategies

- Balance training samples across neighbourhoods.
- Use stratified validation.
- Continuously retrain models using recent data.

## 12. Limitations and Future Improvements

## Engineering Decision Log
Decision:
Random Forest was selected as the primary model because it captured non-linear relationships between property characteristics and prices.

Alternatives considered:
Linear Regression and Gradient Boosting.

Trade-off:
Random Forest provides better accuracy but has lower interpretability compared with linear models.
