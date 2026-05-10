import requests
import pandas as pd
import psycopg2
import logging
from config import DATABASE_URL
from psycopg2.extras import execute_values
from datetime import datetime, timezone

URL = "https://api.coinlore.net/api/tickers/?start=0&limit=10"

def load_coin_lore(URL: str):
    data = {}
    response = requests.get(URL)
    data_lore = response.json()
    data['coin_lore'] = data_lore
    return data

def transfor_lore(data: dict):
    columns = ['name', 'rank', 'price_usd', 'percent_change_24h', 'market_cap_usd']
    df = pd.DataFrame(data["coin_lore"]["data"])

    df = df[columns].copy()
    
    df['date'] = datetime.now(timezone.utc)
    
    return df

def loads(data: pd.DataFrame):
    rows = data.values.tolist()
    sql = 'INSERT INTO row.coin_lore (name, rank, price_usd, percent_change_24h, market_cap_usd, date) VALUES %s'
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            execute_values(cur, sql, rows)
            logging.info(f'[LOAD] rows prepared: {len(rows)}')
clean_df = transfor_lore(load_coin_lore(URL))
loads(clean_df)