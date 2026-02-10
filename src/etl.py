import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
DB_PASS = os.getenv("DB_PASS")
URL = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&names=Bitcoin&symbols=btc"
HEADERS = {"x-cg-api-key": API_KEY}


DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", DB_PASS)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "etl_coins")

def extract_price(url: str):
    response = requests.get(url, headers=HEADERS)
    return response.json()

print(extract_price(URL))
