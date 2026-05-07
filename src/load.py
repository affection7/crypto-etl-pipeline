import pandas as pd
import psycopg2
import logging
from config import DB_URL
from psycopg2.extras import execute_values

def load_to(df: pd.DataFrame):
    with open(file='sql/insert_coins.sql') as f_sql:
        sql = f_sql.read()

    if df.empty:
        logging.info("[LOAD] No rows to load!!!")
        return

    rows = df[["date", "price", "coin", "source"]].values.tolist()

    with psycopg2.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            execute_values(cur, sql, rows)
            logging.info(f'[LOAD] rows prepared: {len(rows)}')