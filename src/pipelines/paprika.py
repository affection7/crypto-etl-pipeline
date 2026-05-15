import logging

from sources.paprika import extract_paprika
from transforms.paprika import transform_price
from loaders.load import load_to
from config import URL_PAPRIKA

def run_paprika_pipelines():
    try:
        data = extract_paprika(URL_PAPRIKA)
        data_clean = transform_price(data)
        load_to(data_clean, "sql/insert_coins.sql", ["date", "price", "coin", "source"])
    except Exception as e:
        logging.error(f"Paprika pipeline failed: {e}")