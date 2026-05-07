import logging
from config import URL_GECKO, URL_PAPRIKA, HEADERS
from extract import extract_price
from transform import transform_price
from load import load_to

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.debug("[EXTRACT] start")
    data = extract_price(URL_GECKO, HEADERS, URL_PAPRIKA)
    logging.debug("[TRANSFORM] start")
    data_df = transform_price(data)
    logging.debug("[LOAD] start")
    load_to(data_df)
    logging.debug("[PIPELINE] done")
 