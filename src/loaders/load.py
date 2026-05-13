import pandas as pd
import psycopg2
import logging
from config import DATABASE_URL
from psycopg2.extras import execute_values

def load_to(df: pd.DataFrame, sql_path: str, columns: list[str]):
    with open(file=sql_path) as f_sql:
        sql = f_sql.read()

    rows = df[columns].values.tolist()

    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            execute_values(cur, sql, rows)
            logging.info(f'[LOAD] rows prepared: {len(rows)}')