# Data Quality Report

## Overview
This report summarizes data quality issues found in the Inside Airbnb dataset.

---

## Missing Values
- Host response rate contains significant missing values
- License field is sparsely populated
- Review-related fields are missing for new listings

---

## Duplicates
- No duplicate listing IDs found in listings dataset
- Calendar dataset requires composite key validation (listing_id + date)

---

## Outliers
- Price contains extreme values that require capping or transformation
- Some listings show unusually high availability patterns

---

## Data Integrity Checks
- All calendar and review records map correctly to listings
- Foreign key relationships validated successfully
