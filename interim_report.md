# Customer Experience Analytics for Fintech Apps  
## Interim Report – Week 2 Challenge  

---

## 1. Project Overview  
This project analyzes Google Play Store reviews of Ethiopian banking mobile applications: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank.  

The goal is to transform raw user reviews into structured insights that help banks understand user satisfaction, complaints, and feature expectations.

---

## 2. Data Collection  
Data was collected using the `google-play-scraper` Python library.  

### Apps analyzed:
- CBE Mobile Banking
- BOA Mobile Banking
- Dashen SuperApp

### Fields collected:
- Review text
- Rating (1–5 stars)
- Date of review
- Bank name
- Source (Google Play Store)

### Scraping method:
- Sorted by newest reviews
- Country: Ethiopia (et)
- Language: English

---

## 3. Dataset Summary  
A total of **1478 reviews** were collected:

- CBE: 482 reviews  
- BOA: 498 reviews  
- Dashen: 498 reviews  

This meets the minimum requirement of 1200+ reviews.

---

## 4. Data Preprocessing  
The dataset was cleaned using Python:
- Removed duplicate reviews
- Removed missing values (null reviews or ratings)
- Standardized date format to YYYY-MM-DD
- Final dataset stored as CSV file in `data/raw/`

---

## 5. Early Insights  
Initial analysis shows variation in user satisfaction across banks based on ratings.

- BOA and Dashen have slightly higher review counts and more consistent user feedback
- CBE shows slightly lower review count but still within expected range

Further analysis will include sentiment classification and thematic clustering.

---

## 6. Challenges  
- Google Play scraping limitations restricted deeper historical data access
- Some variation in available review volume per app
- Rate limits required careful adjustment of scraping size

---

## 7. Next Steps  
The next phase of the project will include:
- Sentiment analysis using NLP models (DistilBERT / VADER)
- Theme extraction using TF-IDF and spaCy
- Storage of processed data in PostgreSQL database
- Data visualization and business insights generation

---

## 8. Conclusion  
This interim stage successfully completed data collection and preprocessing. The dataset is now ready for advanced NLP analysis and database engineering tasks in the next phases.