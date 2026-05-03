import os
from extract import extract_price
from transform import transform_price
from load import load_to
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL_GECKO  = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin,ethereum,solana&names=Bitcoin&symbols=btc"
URL_PAPRIKA = "https://api.coinpaprika.com/v1/tickers/ton-toncoin"
HEADERS = {"x-cg-api-key": API_KEY}

if __name__ == "__main__":
    print("[EXTRACT] start")
    data = extract_price(URL_GECKO, HEADERS, URL_PAPRIKA)
    print("[TRANSFORM] start")
    data_df = transform_price(data)
    print("[LOAD] start")
    load_to(data_df)
    print("[PIPELINE] done")
