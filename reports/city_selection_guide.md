# City Selection Guide

---

## 1. Selected Cities

For this analysis, the following cities were selected:

* **New York City (USA)**
* **London (United Kingdom)**
* **Paris (France)**

These cities represent diverse global Airbnb markets with varying demand patterns, pricing structures, and regulatory environments.

---

## 2. Rationale for City Selection

The selected cities were chosen to ensure diversity in market behavior and to enable meaningful cross-city comparison.

### Key reasons:

* **Market Structure Diversity**

  * New York City: Highly competitive and dynamic market
  * London: Regulated short-term rental environment
  * Paris: Tourism-driven seasonal demand market

* **Demand Behavior Differences**

  * NYC: Business + tourism mixed demand
  * London: Balanced long-term and short-term stays
  * Paris: Strong seasonal tourism concentration

* **Global Relevance**
  These cities are among the most active Airbnb markets globally, making insights more generalizable and business-relevant.

* **Data Richness**
  Each city provides sufficient listing volume and review data to support robust analytics and machine learning modeling.

---

## 3. Data Engineering Considerations

To ensure scalability and consistency across multiple cities, the data pipeline was designed with a modular and configuration-driven approach.

### Key design principles:

* A unified ETL pipeline processes all city datasets using the same logic.
* City name is passed as a parameter to ensure reusability.
* Standard schema mapping is applied across all datasets.
* Consistent feature engineering steps are maintained across cities.
* All outputs are stored in a unified master dataset format.

This design ensures that the system can scale from a few cities to dozens of cities without modifying the core processing logic.

---

## 4. Observed Dataset Differences

During data integration, several inconsistencies were observed across city datasets:

### Common differences:

* Variations in available columns across datasets
* Inconsistent naming conventions for neighborhoods
* Differences in encoding formats and data types
* Missing values in review-related fields
* Variability in host-related attributes

### Handling strategy:

To address these inconsistencies, the following approaches were applied:

* Standardized schema mapping across all cities
* Column normalization and renaming conventions
* Consistent missing value imputation strategies
* Feature alignment to ensure comparability

These steps ensured that all city datasets could be reliably merged into a unified analytical structure.

---

## 5. Cross-City Comparison Framework

To analyze differences between cities, the following key dimensions were used:

### 1. Pricing Structure

* Average price per night
* Price distribution across property types
* Luxury vs budget segment proportions

### 2. Listing Density

* Total number of active listings per city
* Market saturation levels

### 3. Demand Patterns

* Availability trends over time
* Seasonal variations in occupancy behavior

### 4. Review Performance

* Average review scores
* Sentiment distribution from guest reviews

### 5. Host Behavior

* Distribution of superhosts vs regular hosts
* Frequency of listings per host

This framework enables consistent comparison across different urban Airbnb markets.

---

## 6. Scalability Strategy

The system was designed to support horizontal scalability across multiple cities.

### Key scalability features:

* ETL pipeline is fully parameterized by city name
* Modular ingestion process supports additional datasets without code changes
* Standardized schema ensures compatibility across all cities
* Unified master dataset allows centralized analytics and modeling

### Outcome:

This architecture enables expansion from a small number of cities to 50+ cities with minimal engineering effort, demonstrating strong data pipeline scalability principles.

---

## 7. Example Multi-City Data Processing (Optional Implementation)

```python
cities = ["new_york", "london", "paris"]

city_data = {}

for city in cities:
    df = pd.read_csv(f"data/{city}/listings.csv")
    df["city"] = city
    city_data[city] = df
```

---

## Combined Dataset Creation

```python
combined_df = pd.concat(city_data.values(), ignore_index=True)
```

---

## Basic Cross-City Analysis

```python
combined_df.groupby("city")["price_clean"].mean()
```

---

## 8. Key Insights from Multi-City Design

The multi-city approach provides several advantages:

* Enables benchmarking across global Airbnb markets
* Improves generalization of machine learning models
* Enhances robustness of pricing and demand analysis
* Supports scalable data engineering architecture design

---

## 9. Conclusion

The selection of New York City, London, and Paris enables a balanced and diverse analysis of global Airbnb markets.

By designing a scalable and standardized data pipeline, the system is capable of handling multiple cities efficiently while maintaining consistency in analytics, machine learning, and reporting.

This approach demonstrates strong data engineering principles, including modular design, scalability, and cross-domain generalization.
