import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import execute_values

load_dotenv()

DB_PASS = os.getenv("DB_PASS")
DB_URL = f"postgresql://neondb_owner:{DB_PASS}@ep-shiny-firefly-ah7am9sh-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&connect_timeout=10"

def load_to(df: pd.DataFrame):
    with open(file='sql/insert_coins.sql') as f_sql:
        sql = f_sql.read()

    if df.empty:
        print("[LOAD] No rows to load!!!")
        return

    rows = df[["date", "price", "coin"]].values.tolist()

    with psycopg2.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            execute_values(cur, sql, rows)
            print(f'[LOAD] rows prepared: {len(rows)}')