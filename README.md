Task 1: Data Collection & Preprocessing
📥 Data Collection

Reviews were scraped using the google-play-scraper Python library.

📊 Dataset
1500+ reviews collected
Fields included:
review text
rating
date
bank name
source
🧹 Preprocessing
Removed duplicate reviews
Removed missing values
Normalized date formats
🛠 Tools Used
Python
pandas
google-play-scraper
VS Code
💾 Output

Cleaned dataset saved as:

data/raw/reviews.csv
🧠 Task 2: Sentiment & Thematic Analysis
😊 Sentiment Analysis

Implemented using VADER sentiment analysis.

Each review is classified into:

Positive
Neutral
Negative
Output Columns Added:
sentiment_label
sentiment_score
🔍 Thematic Analysis

Keyword-based theme extraction used to identify common issues:

Identified Themes:
Login issues
Transaction delays
OTP/authentication problems
App crashes/stability issues
UI/UX feedback

🗄️ Task 3: PostgreSQL Data Storage
🧱 Database Setup
Database name: bank_reviews
🏦 Tables Design
Banks Table
bank_id (PRIMARY KEY)
bank_name
app_name
Reviews Table
review_id (PRIMARY KEY)
bank_id (FOREIGN KEY)
review_text
rating
review_date
sentiment_label
sentiment_score
identified_theme
source
⚙️ Data Insertion
Implemented using Python (psycopg2)
Script: scripts/load_to_postgres.py
Total inserted records: 1478 reviews
🔍 Verification Queries
-- Count reviews per bank
SELECT bank_id, COUNT(*) 
FROM reviews 
GROUP BY bank_id;

-- Average rating per bank
SELECT bank_id, AVG(rating) 
FROM reviews 
GROUP BY bank_id;

-- Check missing values
SELECT * 
FROM reviews 
WHERE review_text IS NULL 
   OR rating IS NULL;
✅ Result
PostgreSQL database successfully created
Data inserted successfully
Data integrity verified

📊 Task 4: Insights & Recommendations
📈 Analysis Per Bank
🏦 Commercial Bank of Ethiopia (CBE)

Drivers:

Fast transaction processing
Simple UI navigation

Pain Points:

OTP verification delays
Occasional login failures

Recommendations:

Improve OTP delivery system
Strengthen login stability
🏦 Bank of Abyssinia (BOA)

Drivers:

Good user interface
Smooth balance checking

Pain Points:

App crashes during peak usage
Slow transfers

Recommendations:

Improve backend scalability
Optimize transaction system
🏦 Dashen Bank

Drivers:

Easy registration process
Useful banking features

Pain Points:

Poor app stability
Delayed notifications

Recommendations:

Fix crash issues
Improve notification system

📊 Visualizations (Planned/Implemented)
Sentiment distribution per bank
Rating distribution per bank

Theme frequency analysis
📌 Final Outcome

End-to-end data pipeline built
Sentiment + thematic analysis completed
Data stored in PostgreSQL
Business insights generated
Visual analytics prepared

🚀 Tools Used (Full Project)

Python
pandas
VADER (NLTK)
PostgreSQL
psycopg2
matplotlib / seaborn
google-play-scraper
VS Code