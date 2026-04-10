import requests
import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")
DB_PASS = os.getenv("DB_PASS")
URL = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin,ethereum,solana&names=Bitcoin&symbols=btc"
HEADERS = {"x-cg-api-key": API_KEY}

DB_URL = f"postgresql://neondb_owner:{DB_PASS}@ep-shiny-firefly-ah7am9sh-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&connect_timeout=10"

def extract_price(url: str):
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    return data

def transform_price(data: dict):
    rows = []
    date = datetime.now()
    
    for x, y in data.items():
        rows.append({"date": date, "coin": x, "price": y['usd']})
    return pd.DataFrame(rows)

def load_to(df: pd.DataFrame):
    df.to_csv('out.csv', mode='a', index=False, header=False)

    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS bitcoin_prices (id SERIAL PRIMARY KEY, date TIMESTAMP, price FLOAT, coin VARCHAR);")

    for x in range(len(df)):
        value_price = float(df['price'].iloc[x])
        value_coin = df["coin"].iloc[x]
        value_date = df['date'].iloc[x]
        cur.execute("INSERT INTO bitcoin_prices (date, price, coin) VALUES (%s,%s,%s)", (value_date, value_price, value_coin))
        print(f"----- SAVED -----\n PRICE: {value_price}\n TIME: {value_date}\n COIN: {value_coin}")

    conn.commit()
    cur.close()
    conn.close()

try:
    data = extract_price(URL)
    data_df = transform_price(data)
    load_to(data_df)
except:
    print("ERROR")
