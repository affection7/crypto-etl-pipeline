import pandas as pd
from datetime import datetime

def transform_price(data: dict):
    rows = []
    date = datetime.now()
    
    for coin, price in data.items():
        rows.append({"date": date, "price": price['usd'], "coin": coin})
    return pd.DataFrame(rows)