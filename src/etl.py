import requests
import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")
DB_PASS = os.getenv("DB_PASS")
URL = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&names=Bitcoin&symbols=btc"
HEADERS = {"x-cg-api-key": API_KEY}

DB_URL = f"postgresql://neondb_owner:{DB_PASS}@ep-shiny-firefly-ah7am9sh-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&connect_timeout=10"

def extract_price(url: str):
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    return data

def transform_price(data: dict):
    price = data['bitcoin']['usd']
    date = datetime.now()
    return pd.DataFrame({"date": [date], "price": [price]})

def load_to(df: pd.DataFrame):
    df.to_csv('out.csv', mode='a', index=False, header=False)

    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    value_date = df['date'].iloc[0]
    value_price = float(df['price'].iloc[0])

    cur.execute("CREATE TABLE IF NOT EXISTS bitcoin_prices (id SERIAL PRIMARY KEY, date TIMESTAMP, price FLOAT);")
    cur.execute("INSERT INTO bitcoin_prices (date, price) VALUES (%s,%s)", (value_date, value_price))

    conn.commit()
    cur.close()
    conn.close()
    print(f"----- SAVED \n PRICE: {value_price} ----- TIME: {value_date}")

try:
    data = extract_price(URL)
    data_df = transform_price(data)
    load_to(data_df)
except:
    print("ERROR")
