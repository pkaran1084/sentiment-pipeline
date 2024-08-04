import sqlite3
from datetime import datetime
import logging
from tabulate import tabulate

# Create a logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def persist_data(df):
    conn = sqlite3.connect('sentiment_scores.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scores (ticker TEXT, sentiment_score REAL,  date DATE)''')

    for index, row in df.iterrows():
        logger.info(f"title: {row['title']}, link: {row['url']}, sentiment_score: {row['sentiment_score']}")
        c.execute(f"INSERT INTO scores VALUES ('{row['title']}', {row['sentiment_score']}, ?)", (datetime.now().date(),))
    conn.commit()
    conn.close()

    print("\n\nSentiment scores for the news articles")
    print(tabulate(df[["title", "sentiment_score","query"]], headers='keys', tablefmt='grid'))

# To check the values stored in DB
# import sqlite3
# conn = sqlite3.connect('sentiment_scores.db')
# c = conn.cursor()
# c.execute(f"select * from scores")
# c.fetchall()