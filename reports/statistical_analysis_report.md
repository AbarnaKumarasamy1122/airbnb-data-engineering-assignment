
# Airbnb Listing Price Analysis Report

## 1. Introduction
This report presents a statistical analysis of Airbnb listing data, focusing on factors influencing listing prices. We explore various hypotheses related to room types, superhost status, review volume, neighborhood, and seasonality, using statistical tests like t-tests and ANOVA. We also examine feature correlations, build a regression model, and assess multicollinearity to understand key drivers of pricing.

## 2. Hypothesis Testing

### H1: Do entire homes cost more than private rooms?

**Statistical Hypothesis:**
*   **Null (H0):** Mean price of entire homes = Mean price of private rooms.
*   **Alternative (H1):** Mean price of entire homes > Mean price of private rooms.

**Test Used:** Independent two-sample t-test (unequal variance)

**Results:**
*   **t-statistic:** 17.84
*   **p-value:** 6.53e-66
*   **Cohen's d:** 0.69

**Business Interpretation:**
Entire homes have a statistically significant price premium compared with private rooms (p < 0.001, Cohen's d = 0.69, indicating a moderate to large effect size). This supports differentiated pricing strategies and suggests travelers are willing to pay more for privacy and exclusive space. Owners of entire homes can leverage this by highlighting their unique value proposition.

### H2: Does Superhost status impact review scores?

**Statistical Hypothesis:**
*   **Null (H0):** Mean review scores of Superhosts = Mean review scores of non-Superhosts.
*   **Alternative (H1):** Mean review scores of Superhosts ≠ Mean review scores of non-Superhosts.

**Test Used:** Independent two-sample t-test (unequal variance)

**Results:**
*   **t-statistic:** 28.42
*   **p-value:** 1.53e-146
*   **Cohen's d:** 1.07

**Business Interpretation:**
Superhosts have statistically significantly higher review scores than non-Superhosts (p < 0.001, Cohen's d = 1.07, indicating a large effect size). If significant, the Superhost badge appears associated with improved guest experience and may influence customer trust, leading to higher bookings or potentially higher prices. Platforms could promote Superhost criteria more actively.

### H3: Is there a price difference for listings with high versus low review counts?

**Statistical Hypothesis:**
*   **Null (H0):** Mean price of high review listings = Mean price of low review listings.
*   **Alternative (H1):** Mean price of high review listings ≠ Mean price of low review listings.

**Test Used:** Independent two-sample t-test (unequal variance)

**Results:**
*   **t-statistic:** -4.39
*   **p-value:** 1.43e-05
*   **Cohen's d:** -0.30

**Business Interpretation:**
Listings with high review counts ( > 10 reviews) have statistically significantly lower prices than those with low review counts ( <= 10 reviews) (p < 0.001, Cohen's d = -0.30, indicating a small to moderate effect size). Review volume may act as a proxy for demand. This suggests that highly reviewed listings might be more competitive on price, or that lower prices lead to more reviews. This could also indicate that very popular listings don't necessarily charge premiums.

### H4: Do neighbourhood prices differ?

**Statistical Hypothesis:**
*   **Null (H0):** All top 10 neighbourhoods have the same average price.
*   **Alternative (H1):** At least one neighbourhood has a different average price.

**Test Used:** One-way ANOVA

**Results:**
*   **F-statistic:** 12.93
*   **p-value:** 4.99e-20
*   **Eta-squared:** 0.0719

**Business Interpretation:**
There are statistically significant differences in average prices among the top 10 neighbourhoods (p < 0.001, Eta-squared = 0.0719). This indicates that location is a major pricing driver, accounting for approximately 7.2% of the variance in price. Property managers and hosts should tailor pricing strategies based on the specific neighborhood's market value.

### H5: Do weekend prices differ from weekday prices?

**Statistical Hypothesis:**
*   **Null (H0):** Mean weekend price = Mean weekday price.
*   **Alternative (H1):** Mean weekend price ≠ Mean weekday price.

**Test Used:** Independent two-sample t-test (unequal variance)

**Results:**
*   **t-statistic:** NaN
*   **p-value:** NaN
*   **Cohen's d:** 1.26e-08

**Business Interpretation:**
While Cohen's d is very small (1.26e-08), the t-test returned NaN values, which suggests an issue with the data for this specific comparison (likely all values were identical after cleaning, resulting in zero variance). Assuming a meaningful difference exists based on general market trends, higher weekend prices would indicate strong leisure demand and justify dynamic pricing strategies. Further investigation into the NaN result is needed.

## 3. Confidence Intervals and Effect Sizes

**Confidence Intervals for `price_clean` by `room_type`:**

| room_type       | mean      | count | std        | margin_error | CI_lower  | CI_upper  |
|:----------------|:----------|:------|:-----------|:-------------|:----------|:----------|
| Entire home/apt | 426.1371  | 1384  | 346.4497   | 18.2527      | 407.8844  | 444.3899  |
| Hotel room      | 562.9964  | 56    | 360.8808   | 94.5205      | 468.4760  | 657.5169  |
| Private room    | 245.2313  | 1945  | 177.2369   | 7.8768       | 237.3545  | 253.1081  |
| Shared room     | 388.7958  | 48    | 504.5859   | 142.7482     | 246.0477  | 531.5440  |

These confidence intervals provide a range within which the true mean price for each room type is likely to fall. The wider intervals for 'Hotel room' and 'Shared room' indicate higher variability or smaller sample sizes compared to 'Entire home/apt' and 'Private room'.

**Effect Sizes Summary (Cohen's d & Eta-squared):**

*   **H1 (Entire vs. Private room price):** Cohen's d = 0.69 (Moderate to Large effect)
*   **H2 (Superhost vs. non-Superhost review scores):** Cohen's d = 1.07 (Large effect)
*   **H3 (High vs. Low reviews price):** Cohen's d = -0.30 (Small to Moderate effect)
*   **H4 (Neighbourhood vs. price):** Eta-squared = 0.0719 (Explains about 7.2% of variance)
*   **H5 (Weekend vs. Weekday price):** Cohen's d = 1.26e-08 (Negligible effect, but results are NaN)

## 4. Correlation and Driver Analysis

**Feature Correlation Matrix:**

```
                      price_clean  accommodates      beds  bedrooms  \nprice_clean              1.000000      0.529556  0.497549  0.560335   \naccommodates             0.529556      1.000000  0.765146  0.626290   \nbeds                     0.497549      0.765146  1.000000  0.698790   \nbedrooms                 0.560335      0.626290  0.698790  1.000000   \nnumber_of_reviews       -0.111910     -0.119099 -0.066161 -0.080101   \nreview_scores_rating     0.068400     -0.097905 -0.007575  0.098900   \n
                      number_of_reviews  review_scores_rating  
price_clean                   -0.111910              0.068400  
accommodates                  -0.119099             -0.097905  
beds                          -0.066161             -0.007575  
bedrooms                      -0.080101              0.098900  
number_of_reviews              1.000000              0.059098  
review_scores_rating           0.059098              1.000000  
```

**Business Interpretation:**
Strong positive correlations are observed between `price_clean` and `accommodates`, `beds`, and `bedrooms`. This suggests that variables influencing pricing, such as property capacity and bedroom count, are significant drivers of listing price. `number_of_reviews` shows a slight negative correlation with price, while `review_scores_rating` has a weak positive correlation.

**Accommodation Capacity vs Price:**

The scatter plot with a lowess regression line shows a general upward trend, indicating that as accommodation capacity (`accommodates`) increases, the `price_clean` also tends to increase, although with considerable variability at higher capacities.

## 5. Regression Findings

**OLS Regression Results:**

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:            price_clean   R-squared:                       0.373
Model:                            OLS   Adj. R-squared:                  0.372
Method:                 Least Squares   F-statistic:                     408.0
Date:                Mon, 22 Jun 2026   Prob (F-statistic):               0.00
Time:                        05:38:31   Log-Likelihood:                -23458.
No. Observations:                3433   AIC:                         4.693e+04
Df Residuals:                    3427   BIC:                         4.696e+04
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept             -243.7182     69.668     -3.498      0.000    -380.313    -107.124
accommodates            34.9967      2.653     13.189      0.000      29.794      40.199
bedrooms                97.7661      5.526     17.692      0.000      86.931     108.601
beds                     6.0005      4.477      1.340      0.180      -2.777      14.778
number_of_reviews       -0.0927      0.025     -3.776      0.000      -0.141      -0.045
review_scores_rating    68.6023     14.549      4.715      0.000      40.077      97.127
==============================================================================
Omnibus:                     3399.542   Durbin-Watson:                   1.771
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           302191.084
Skew:                           4.608   Prob(JB):                         0.00
Kurtosis:                      48.030   Cond. No.                     3.57e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.57e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

**Business Interpretation:**
The regression model explains approximately 37.3% of the variance in `price_clean` (R-squared = 0.373). Key findings include:

*   A positive `bedrooms` coefficient (97.77) indicates that, holding other factors constant, each additional bedroom increases the price by approximately $97.77. This is a strong indicator of property size and value.
*   Similarly, `accommodates` has a positive coefficient (35.00), suggesting that listings designed for more guests command higher prices.
*   `review_scores_rating` also shows a positive and significant coefficient (68.60), implying that higher guest ratings are associated with higher prices, potentially reflecting perceived quality or host reputation.
*   `number_of_reviews` has a small but statistically significant negative coefficient (-0.09), suggesting that higher review counts are associated with slightly lower prices, consistent with the correlation analysis.
*   `beds` is not statistically significant (p = 0.180) in this model after accounting for other variables, suggesting its effect on price is captured by `accommodates` and `bedrooms`.

This model helps identify factors that drive pricing, allowing hosts to strategically adjust features or marketing to optimize revenue.

## 6. Multicollinearity Assessment

**Variance Inflation Factor (VIF) Results:**

```
                feature         VIF
0                 const  329.923401
1          accommodates    2.613999
2              bedrooms    2.105218
3                  beds    2.990366
4     number_of_reviews    1.019208
5  review_scores_rating    1.057578
```

**Interpretation:**

*   **VIF < 5:** Acceptable levels of multicollinearity.
*   **VIF 5–10:** Moderate multicollinearity.
*   **VIF > 10:** Serious multicollinearity.

The VIF values for `accommodates`, `bedrooms`, `beds`, `number_of_reviews`, and `review_scores_rating` are all well below 5. This indicates that multicollinearity among these predictor variables is not a significant concern in our regression model, suggesting that their independent effects on `price_clean` can be reliably estimated.

## 7. Business Recommendations
*   **Dynamic Pricing:** Leverage insights from H1 (entire homes vs. private rooms) and H4 (neighborhoods) to implement dynamic pricing strategies. Charge premiums for entire homes and in high-demand neighborhoods.
*   **Superhost Program:** Encourage and support hosts in achieving/maintaining Superhost status, as it significantly correlates with higher review scores, which can build trust and potentially lead to better occupancy rates.
*   **Property Features:** For hosts looking to increase price, focus on increasing `accommodates` and `bedrooms` (e.g., adding beds or converting rooms if feasible).
*   **Review Strategy:** Investigate the negative correlation between `number_of_reviews` and `price_clean`. This might suggest that new listings can command higher prices, or that highly-reviewed listings are priced competitively. Hosts might need to balance pricing and review generation.
*   **Weekend Pricing:** While the t-test for weekend vs. weekday prices was inconclusive (NaN), typical leisure travel patterns suggest potential for higher weekend pricing. Further investigation with more robust data or a different approach is warranted to confirm this.

## 8. Statistical Limitations
*   **Unexplained Variance:** The regression model (R-squared = 0.373) only explains a moderate portion of the price variance. Many other factors not included in this analysis (e.g., specific amenities, host response time, cancellation policy, local events, time of year, property condition, detailed location within a neighborhood) likely influence pricing.
*   **Data Specificity:** The analysis is based on New York City Airbnb data. The findings may not be generalizable to other cities or regions with different market dynamics, regulations, or traveler preferences.
*   **Missing Data Handling:** Dropping rows with `NaN` values in `analysis_df` could introduce selection bias if the missingness is not completely at random.
*   **Weekend/Weekday Price Comparison Issue:** The t-test for weekend vs. weekday prices yielded NaN values, indicating a potential data issue (e.g., all prices were identical, leading to zero variance for one or both groups). This specific hypothesis test result is not reliable and requires further data investigation.
*   **Causality vs. Correlation:** While the analysis identifies correlations and statistical significance, it does not strictly imply causality. For example, higher review scores might lead to higher prices, but it's also possible that higher-quality (and thus higher-priced) listings naturally attract better reviews.
