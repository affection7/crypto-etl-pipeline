from extract import extract_price
from transform import transform_price
from load import load_to


URL = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin,ethereum,solana&names=Bitcoin&symbols=btc"
if __name__ == "__main__":
    try:
        data = extract_price(URL)
        data_df = transform_price(data)
        load_to(data_df)
    except:
        print("ERROR")