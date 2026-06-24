# Airbnb Market Intelligence Platform

### Expernetic Data Engineering Intern Assignment

## 1. Project Overview

This project presents an end-to-end data engineering, analytics, data science, and AI-driven market intelligence solution built using the Inside Airbnb dataset.

The objective of the project is to transform raw Airbnb data into actionable business insights through:

* Automated data ingestion and cleaning pipelines
* Exploratory data analysis and statistical validation
* Machine learning-based price prediction
* Customer and listing segmentation
* Natural Language Processing (NLP) on guest reviews
* AI-powered recommendation and market intelligence systems
* Scalable architecture design for multi-city analysis

The project demonstrates practical skills in data engineering, analytics, machine learning, Generative AI, and production-oriented system design.

---

# 2. Selected Cities

The analysis focuses on the following Airbnb markets:

* New York City (USA)
* London (United Kingdom)
* Paris (France)

These cities were selected to demonstrate cross-city analysis, scalable data pipelines, and comparative market intelligence.

---

# 3. Repository Structure

```
airbnb-market-intelligence/
│
├── README.md
│
├── notebooks/
│   ├── 01_dataset_familiarization.ipynb
│   ├── 02_data_quality_report.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_statistical_analysis.ipynb
│   ├── 05_data_science_challenges.ipynb
│   ├── 06_ai_ml_opportunities.ipynb
│   ├── 07_open_innovation.ipynb
│   └── 08_city_selection_analysis.ipynb
│
│
├── reports/
│
├── pipelines/
|
│
├── requirements.txt
└── .gitignore
```

---

# 4. Technology Stack

## Programming and Data Processing

* Python
* Pandas
* NumPy
* DuckDB
* SQL

## Data Visualization

* Matplotlib
* Seaborn
* Plotly
* Streamlit

## Machine Learning and Statistics

* Scikit-learn
* StatsModels
* SciPy
* SHAP

## Natural Language Processing and Generative AI

* TextBlob
* spaCy
* TF-IDF Vectorization
* LLM-based insight generation
* RAG architecture design

## Development Tools

* Git
* GitHub
* Jupyter Notebook

---

# 5. Dataset

Data was collected from the Inside Airbnb open dataset.

The following files were used:

* listings.csv.gz — Listing information
* calendar.csv.gz — Daily pricing and availability
* reviews.csv.gz — Guest review records
* neighbourhoods.csv — Geographical reference information

The datasets were integrated using listing identifiers to create a unified analytical dataset.

---

# 6. Project Workflow

The project follows a complete data lifecycle:

```
Raw Airbnb Data
        ↓
Data Ingestion
        ↓
Data Cleaning and Validation
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Statistical Testing
        ↓
Machine Learning Models
        ↓
NLP and AI Experiments
        ↓
Recommendation System
        ↓
AI Market Intelligence Assistant
        ↓
Business Insights and Reporting
```

---

# 7. Environment Setup

## 1. Clone the Repository

```bash
git clone <repository-url>
cd airbnb-market-intelligence
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 8. Data Preparation

Download Airbnb datasets and place them inside:

```
data/raw/
```

Example:

```
data/raw/new_york/listings.csv.gz
data/raw/new_york/calendar.csv.gz
data/raw/new_york/reviews.csv.gz
```

Repeat the same structure for all selected cities.

---

# 9. Execution Order

The recommended order for reviewing and running the project is:

## Step 1 — Data Understanding

```
notebooks/01_data_exploration.ipynb
```

Purpose:

* Understand dataset structure
* Explore missing values
* Validate relationships

---

## Step 2 — Data Cleaning

```
notebooks/02_data_cleaning.ipynb
```

Purpose:

* Handle missing values
* Convert price and percentage fields
* Standardize schemas

---

## Step 3 — Exploratory Data Analysis

```
notebooks/03_exploratory_analysis.ipynb
```

Purpose:

* Analyze pricing trends
* Study neighborhoods
* Explore host and demand patterns

---

## Step 4 — Statistical Analysis

```
notebooks/04_statistical_analysis.ipynb
```

Purpose:

* Hypothesis testing
* Confidence intervals
* Effect size calculations
* Regression analysis

---

## Step 5 — Machine Learning

```
notebooks/05_machine_learning.ipynb
```

Purpose:

* Feature engineering
* Model training
* Model evaluation
* Explainability analysis

---

## Step 6 — NLP and AI Experiments

```
notebooks/06_nlp_and_ai_experiments.ipynb
```

Purpose:

* Sentiment analysis
* Topic modeling
* Named Entity Recognition
* LLM application design

---

## Step 7 — Recommendation System

```
notebooks/07_recommendation_system.ipynb
```

Purpose:

* Content-based recommendations
* TF-IDF feature extraction
* Nearest-neighbor similarity search

---

## Step 8 — Open Innovation Solution

```
notebooks/08_open_innovation_assistant.ipynb
```

Purpose:

* AI-powered market intelligence assistant
* Automated insight generation
* Business recommendation engine

---

# 10. Key Deliverables

The repository contains:

* Complete source code
* Reproducible notebooks
* Data quality assessment
* Engineering decision documentation
* Statistical analysis
* Machine learning experiments
* AI and NLP experiments
* Open innovation solution
* Professional final report
* AI usage disclosure

---

# 11. Key Findings

Major insights obtained from the analysis include:

* Airbnb pricing is highly influenced by property size, location, and room type.
* Entire homes command a significant price premium compared with private rooms.
* Superhost status is strongly associated with higher review scores.
* A small percentage of hosts control a large share of listings, indicating professionalized supply.
* Customer reviews provide valuable signals for service improvement.
* Machine learning models can effectively support data-driven pricing decisions.
* AI assistants can convert complex analytical outputs into understandable business recommendations.

---

# 12. AI Usage Disclosure

AI tools were used responsibly throughout the project to assist with:

* Code generation and optimization
* Documentation improvements
* Architecture brainstorming
* Report writing assistance
* Debugging and troubleshooting

All AI-generated outputs were manually reviewed, tested, modified where necessary, and validated against the dataset and expected analytical results.

The final design decisions, analysis, interpretations, and conclusions remain the responsibility of the author.

---

# 13. Security and Privacy

This repository does not include:

* API keys
* Passwords
* Personal credentials
* Private user information

All sensitive information has been excluded or anonymized before submission.

---

# 14. Future Improvements

Potential future enhancements include:

* Deploying the AI assistant as a production API
* Building a complete RAG-based analytics chatbot
* Integrating real-time Airbnb market updates
* Implementing automated ML monitoring pipelines
* Expanding the system to additional global cities

