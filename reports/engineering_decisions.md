# Engineering Decision Log

## 1. File Format Choice
- Chose pandas for ingestion due to simplicity and dataset size
- Trade-off: Not scalable for big data systems

---

## 2. Cleaning Strategy
- Standardized price into numeric format
- Trade-off: Loss of original formatting information

---

## 3. Data Modeling Choice
- Used DuckDB for lightweight analytical SQL layer
- Trade-off: Not production distributed system (like Spark)

---

## 4. Missing Value Handling
- Left most missing values as null instead of imputation
- Trade-off: Preserves data authenticity but limits ML readiness

---

## 5. Pipeline Design
- Built modular Python classes for reusability
- Trade-off: Not fully production orchestrated (no Airflow)
