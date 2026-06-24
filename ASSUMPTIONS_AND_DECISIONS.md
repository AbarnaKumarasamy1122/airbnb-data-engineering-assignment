# Assumptions & Engineering Decisions Log

## 1. Dataset Assumptions

- Missing values in price were treated as invalid entries and removed
- Reviews represent post-stay feedback, not real-time sentiment
- Availability calendar reflects historical scraping snapshots

---

## 2. Data Engineering Decisions

### Decision: Use single unified master table
- Considered: star schema vs flat table
- Chosen: flat analytical table for simplicity and dashboard compatibility
- Trade-off: less normalized but easier for analytics

---

### Decision: Nearest Neighbors instead of full similarity matrix
- Considered: cosine similarity matrix
- Chosen: NearestNeighbors (memory efficient)
- Trade-off: no full pairwise similarity storage

---

## 3. Machine Learning Decisions

- TF-IDF used for textual feature representation
- Cosine similarity used for recommendation scoring
- Simple models preferred over deep learning due to dataset size

---

## 4. Statistical Decisions

- T-tests used for 2-group comparisons
- ANOVA used for multi-neighbourhood comparisons
- Effect size included to ensure practical significance

---

## 5. Multi-City Strategy

- Selected 2–3 cities instead of 7+
- Reason: balance between depth and scalability demonstration

---

## 6. Key Trade-offs

- Depth > breadth
- Scalability > complexity
- Interpretability > advanced models