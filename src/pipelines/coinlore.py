import logging

from sources.coinlore import extract_coinlore
from transforms.coinlore import transform_price
from loaders.load import load_to
from config import URL_COINLORE

def run_coinlore_pipelines():
    try:
        data = extract_coinlore(URL_COINLORE)
        data_clean = transform_price(data)
        load_to(data_clean, "sql/insert_coins_coinlore.sql", ["date", "nameid", "price", "percent_change_24h", "percent_change_7d", "market_cap_usd", "source"])
    except Exception as e:
        logging.error(f"Coinlore pipeline failed: {e}")