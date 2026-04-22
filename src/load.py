import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASS = os.getenv("DB_PASS")
DB_URL = f"postgresql://neondb_owner:{DB_PASS}@ep-shiny-firefly-ah7am9sh-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&connect_timeout=10"

def load_to(df: pd.DataFrame):

    with open(file='../sql/insert_coins.sql') as f_sql:
        sql = f_sql.read()

    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    for x in range(len(df)):
        value_price = float(df['price'].iloc[x])
        value_coin = df["coin"].iloc[x]
        value_date = df['date'].iloc[x]
        cur.execute(sql, (value_date, value_price, value_coin))
        print(f"----- SAVED -----\n PRICE: {value_price}\n TIME: {value_date}\n COIN: {value_coin}")

    conn.commit()
    cur.close()
    conn.close()