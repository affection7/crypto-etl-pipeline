import pandas as pd
from datetime import datetime

def transform_price(data: dict):
    rows = []
    date = datetime.now()
    
    print("START TRANSFORM")
    for coin, price in data.items():
        rows.append({"date": date, "price": price['usd'], "coin": coin})
    print(f'START EXTRACT {len(data.items())}')
    return pd.DataFrame(rows)