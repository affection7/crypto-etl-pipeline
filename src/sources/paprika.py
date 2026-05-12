
import requests
import logging
from requests.exceptions import HTTPError
import pandas as pd
import logging
from datetime import datetime, timezone

URL = "https://api.coinpaprika.com/v1/tickers/ton-toncoin"

def extract_paprika(url: str) -> list[dict]:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        logging.info("[EXTRACT] paprika success")
        return data
    except HTTPError as http_paprika_error:
        logging.error(f"HTTP ощибка: {http_paprika_error}")

def transform_price(data_list: dict):
    rows = []
    date = datetime.now(timezone.utc)

    rows.append({
        "date": date,
        "price": round(float(data_list["quotes"]["USD"]["price"]),3),
        "coin": data_list["name"].lower(),
        "source": "paprika",

    })

    print(f'[TRANSFORM] processed {len(rows)} coins {rows}')
    return pd.DataFrame(rows)

transform_price(extract_paprika(URL))