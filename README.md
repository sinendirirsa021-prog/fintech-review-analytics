# Fintech Review Analytics

## Objective
Analyze customer reviews from Ethiopian fintech banking apps on the Google Play Store.

## Banks Included
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

## Data Collection
Reviews were scraped using the google-play-scraper Python library.

## Dataset
- 1500+ reviews collected
- Includes:
  - review text
  - rating
  - date
  - bank name
  - source

## Preprocessing
- Removed duplicate reviews
- Removed missing values
- Normalized date format

## Tools Used
- Python
- pandas
- google-play-scraper
- VS Code

## Output
Cleaned dataset saved as:
data/raw/reviews.csv