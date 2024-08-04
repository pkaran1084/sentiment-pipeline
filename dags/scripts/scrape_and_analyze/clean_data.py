import json
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def clean_data(data):
    logger.info("Inside clean data: %s", data)
    # Code to clean and deduplicate the data
    # Remove any leading or trailing whitespace from title and text
    data['title'] = data['title'].str.strip()
    data['text'] = data['text'].str.strip()
    data['url'] = data['url'].str.strip()

    # Convert title and text to lowercase
    data['title'] = data['title'].str.lower()
    data['text'] = data['text'].str.lower()
    data['url'] = data['url'].str.lower()

    # Remove any duplicate rows based on title and text
    # Code to clean and deduplicate the data
    data.drop_duplicates(subset=['title', 'text'], inplace=True)
    data.sort_values(by='publishDate', ascending=False, inplace=True)

    logger.info(data)
    logger.info("End of clean data:")
    return data
