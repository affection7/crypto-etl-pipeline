from extract import extract_price
from transform import transform_price
from load import load_to


URL = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin,ethereum,solana&names=Bitcoin&symbols=btc"
if __name__ == "__main__":
    print("[EXTRACT] start")
    data = extract_price(URL)
    print("[TRANSFORM] start")
    data_df = transform_price(data)
    print("[LOAD] start")
    load_to(data_df)
    print("[PIPELINE] done")
