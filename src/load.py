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

    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    if df.empty:
        print("No rows!!!")
        return
    rows = df[["date", "price", "coin"]].values.tolist()
    execute_values(cur,sql, rows)

    conn.commit()
    cur.close()
    conn.close()