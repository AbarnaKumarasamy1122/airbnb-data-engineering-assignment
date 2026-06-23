## Dataset Selection

The New York City Inside Airbnb dataset was selected for analysis.

The following files were downloaded:

- listings.csv.gz: Detailed information about Airbnb listings
- calendar.csv.gz: Daily availability and pricing data
- reviews.csv.gz: Guest review records
- neighbourhoods.csv: Neighbourhood reference data

Dataset snapshot:

| File | Rows | Columns |
|---|---:|---:|
| listings | 35,036 | 91 |
| calendar | 12,788,141 | 5 |
| reviews | 1,003,299 | 6 |
| neighbourhoods | 230 | 2 |


                 HOST
                   |
                   | host_id
                   |
                LISTINGS
              (id - PK)
                  |
      -----------------------
      |                     |
 listing_id             listing_id
 (FK)                   (FK)
      |                     |
 CALENDAR              REVIEWS

| Dataset        | Primary Key       | Foreign Key              | Relationship                     |
| -------------- | ----------------- | ------------------------ | -------------------------------- |
| Listings       | id                | host_id                  | Each listing belongs to a host   |
| Calendar       | listing_id + date | listing_id → listings.id | Daily availability for a listing |
| Reviews        | id                | listing_id → listings.id | Reviews linked to a listing      |
| Neighbourhoods | neighbourhood     | Used as lookup           | Geographical categorization      |


| Column                  | Explanation                                                                     |
| ----------------------- | ------------------------------------------------------------------------------- |
| price                   | Stored as text with currency symbols, requires cleaning before analysis         |
| host_response_rate      | Percentage stored as string, requires conversion to numeric                     |
| amenities               | Stored as a list-like text field, requires parsing                              |
| availability_365        | Number of available days in the next 365 days, not historical occupancy         |
| estimated_revenue_l365d | Estimated revenue calculated by Inside Airbnb, not actual Airbnb financial data |
| reviews_per_month       | Average monthly review rate, may be unreliable for new listings                 |

## Dataset Limitations

### 1. Scraped Data
The dataset is collected through web scraping and may not perfectly represent Airbnb's internal records.

### 2. Missing Values
Several host and property attributes contain missing values because they are optional or unavailable.

### 3. No Complete Booking History
The calendar dataset provides a snapshot of availability for upcoming dates rather than historical bookings.

### 4. Estimated Metrics
Columns such as estimated occupancy and revenue are model-based estimates from Inside Airbnb and should not be treated as exact financial figures.

### 5. Geographic Coverage
Only listings visible and captured during the scraping date are included.

## Assumptions

1. Listing IDs are assumed to uniquely identify Airbnb properties.

2. Calendar availability is assumed to represent future availability at the time of scraping.

3. Missing values in optional fields such as license or host description do not necessarily indicate poor quality data.

4. Price values represent advertised nightly prices and may not include cleaning fees, taxes, or discounts.

5. Review counts are assumed to represent publicly available guest reviews only.

## Business Domain Understanding

### Listing
A property offered on Airbnb for short-term rental. It contains information about location, pricing, amenities, and capacity.

### Host
An individual or organization responsible for managing one or multiple listings.

### Calendar
A daily operational record showing whether a listing is available and its advertised price.

### Review
Feedback left by guests after completing a stay. Reviews provide signals of quality and customer satisfaction.

### Neighbourhood
A geographic grouping that enables regional analysis of demand, pricing, and supply.

## Conclusion

The New York Airbnb dataset contains 35,036 listings, over 12.7 million daily calendar records, and more than one million guest reviews. The datasets are relationally connected through listing identifiers and provide a strong foundation for building analytical pipelines.

Key engineering observations include the presence of missing values, string-based numerical fields requiring transformation, and estimated metrics requiring careful interpretation. Data quality checks confirmed valid relationships between major datasets.
