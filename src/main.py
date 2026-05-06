import os
import logging
from extract import extract_price
from transform import transform_price
from load import load_to
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL_GECKO  = os.getenv("URL_GECKO")
URL_PAPRIKA = os.getenv("URL_PAPRIKA")
HEADERS = {"x-cg-api-key": API_KEY}

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.debug("[EXTRACT] start")
    data = extract_price(URL_GECKO, HEADERS, URL_PAPRIKA)
    logging.debug("[TRANSFORM] start")
    data_df = transform_price(data)
    logging.debug("[LOAD] start")
    load_to(data_df)
    logging.debug("[PIPELINE] done")
 