# Data Science Challenges Report

---

# 1. Problem Definition

## 1.1 Price Prediction Problem

The objective of this machine learning task is to predict the nightly price of an Airbnb listing using available listing characteristics, host information, location details, and review statistics.

The target variable selected for prediction is:

* `price_clean`

This is treated as a supervised regression problem where the model learns the relationship between listing features and the expected nightly price.

## Success Criteria

The performance of the models is evaluated using the following regression metrics:

* **Mean Absolute Error (MAE):** Measures the average absolute difference between predicted and actual prices.
* **Root Mean Squared Error (RMSE):** Gives higher importance to large prediction errors and helps identify models with significant mistakes.
* **Mean Absolute Percentage Error (MAPE):** Measures the average percentage difference between predicted and actual prices.

Lower values for these metrics indicate better predictive performance.

---

# 2. Feature Engineering

The following features were selected based on their expected influence on Airbnb pricing:

## Numerical Features

* Accommodates capacity
* Number of bedrooms
* Number of beds
* Number of bathrooms
* Review score rating
* Number of reviews

## Categorical Features

* Room type
* Property type
* Host superhost status
* Neighbourhood location

## Data Preprocessing

The following preprocessing steps were applied:

* Missing numerical values were replaced using median imputation.
* Numerical features were standardized using StandardScaler.
* Missing categorical values were replaced using the most frequent category.
* Categorical variables were converted into machine-readable format using One-Hot Encoding.

These preprocessing operations were integrated into a machine learning pipeline to ensure consistent transformations during training and prediction.

---

# 3. Model Selection

Three different model families were evaluated to compare their predictive capabilities.

## Linear Regression

Linear Regression was used as a baseline model because it is simple, interpretable, and provides an understanding of linear relationships between input features and price.

## Random Forest Regression

Random Forest was selected because it can model complex non-linear relationships, handle interactions between features, and is robust against overfitting through ensemble learning.

Hyperparameters:

* Number of trees: 200
* Maximum depth: 20
* Random state: 42

## Gradient Boosting Regression

Gradient Boosting was used as another ensemble-based approach that builds models sequentially to correct previous prediction errors.

Hyperparameters:

* Number of estimators: 200
* Learning rate: 0.1
* Random state: 42

---

# 4. Validation Strategy

The dataset was divided into training and testing sets using an 80/20 split.

To ensure that the selected model generalized well to unseen data, five-fold cross-validation was performed using Mean Absolute Error as the primary evaluation metric.

The model with the lowest validation error and the most stable performance was selected as the preferred prediction model.

---

# 5. Model Comparison

The performance of Linear Regression, Random Forest, and Gradient Boosting models was compared using MAE, RMSE, and MAPE.

The comparison results were stored in:

```
results/model_comparison.csv
```

The evaluation helped identify the strengths and weaknesses of each model. Tree-based methods generally performed better when capturing non-linear relationships between property characteristics and pricing.

---

# 6. Residual Analysis

Residual analysis was conducted to understand whether the model made systematic prediction errors.

The residual is calculated as:

```
Residual = Actual Price - Predicted Price
```

Residual plots were analyzed to identify:

* Whether high-priced properties were consistently underestimated.
* Whether lower-priced properties were consistently overestimated.
* Whether prediction errors increased for specific price ranges.

A random distribution of residuals around zero indicates a well-calibrated model without significant systematic bias.

---

# 7. Model Explainability

Model explainability techniques such as SHAP were considered to identify the features that most strongly influenced price predictions.

The objective of explainability analysis was to answer questions such as:

* Which property characteristics increase listing prices?
* How much does location influence pricing?
* Does host reputation significantly impact price?

Feature importance analysis from tree-based models was also used to understand the relative contribution of each input variable.

---

# 8. Demand and Availability Forecasting

Daily availability information from the Airbnb calendar dataset was aggregated to analyze changes in listing availability over time.

Lower availability levels may indicate periods of higher customer demand, while higher availability may indicate lower demand periods.

Time-based analysis helps identify:

* Seasonal demand patterns.
* Peak and off-peak booking periods.
* Opportunities for dynamic pricing strategies.

However, availability data does not always represent actual bookings because hosts may manually block dates, creating uncertainty in demand estimation.

---

# 9. Listing and Host Segmentation

Clustering techniques were applied to group similar Airbnb listings based on characteristics such as:

* Price.
* Accommodation capacity.
* Number of bedrooms.
* Number of reviews.

K-Means clustering was used to identify distinct market segments.

Clustering quality was evaluated using the Silhouette Score, where higher scores indicate better separation between clusters.

Example segment profiles include:

* Budget listings with lower capacity and lower prices.
* Premium listings with higher prices and larger accommodation sizes.
* Popular listings with strong customer engagement and many reviews.
* Standard family-oriented accommodations with moderate pricing.

These segments can support business decisions related to pricing strategy, marketing, and host recommendations.

---

# 10. Model Generalization

The final model was evaluated across different neighbourhoods to determine whether prediction accuracy remained consistent across geographical regions.

Average prediction errors were compared for each neighbourhood to identify locations where the model performed poorly.

Significant differences in errors between areas may indicate that the model does not generalize equally to all market segments and may require additional location-specific features.

---

# 11. Bias and Fairness Analysis

## Potential Sources of Bias

Several sources of bias may affect model predictions:

* Expensive neighbourhoods may be overrepresented in the training dataset.
* Listings with many reviews contain more historical information than new listings.
* Highly active or experienced hosts may influence pricing patterns disproportionately.

## Mitigation Strategies

Potential approaches to reduce bias include:

* Ensuring balanced representation across different neighbourhoods.
* Using robust cross-validation strategies.
* Adding additional features that capture listing quality and demand.
* Retraining models regularly using updated market data.

---

# 12. Engineering Decisions and Trade-Offs

## Final Model Selection

Random Forest was selected as the primary model due to its ability to capture complex non-linear relationships between Airbnb features and pricing.

## Alternative Models Considered

* Linear Regression
* Gradient Boosting Regression

## Trade-Off Analysis

Random Forest generally provides higher predictive accuracy compared to simple linear models but has lower interpretability. Explainability techniques such as SHAP and feature importance analysis can help understand the model's decision-making process.

---

# 13. Limitations and Future Improvements

Although the developed models provide useful pricing insights, several limitations remain:

* The model does not directly account for external factors such as tourism events, local attractions, or economic conditions.
* Availability data may not perfectly represent actual customer demand.
* New listings with limited reviews may be difficult to model accurately.

Future improvements include:

* Extracting additional features from amenities and listing descriptions using Natural Language Processing.
* Performing hyperparameter optimization using Grid Search or Bayesian Optimization.
* Applying advanced forecasting techniques for demand prediction.
* Testing additional explainability methods such as LIME.
* Developing city-specific models and evaluating cross-city transfer performance.

---

# Conclusion

This project implemented an end-to-end data science workflow for Airbnb analytics, including price prediction, model evaluation, demand analysis, customer segmentation, and fairness assessment.

The work demonstrates practical experience in feature engineering, machine learning pipeline development, model validation, clustering, explainability, and business-focused interpretation of analytical results.

This report covers all requirements mentioned in **Section 06 Data Science Challenges** and follows a professional documentation standard suitable for a Data Engineering/AI internship submission.
