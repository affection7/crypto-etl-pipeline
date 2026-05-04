import pandas as pd
from datetime import datetime, timezone

def transform_price(data_list: list):
    rows = []
    date = datetime.now(timezone.utc)
    
    for item in data_list:
        if "quotes" in item:
            rows.append({
                "date": date, 
                "price": round(item["quotes"]["USD"]["price"], 2), 
                "coin": item["symbol"]
            })
        else:
            for coin, price in item.items():
                rows.append({
                    "date": date, 
                    "price": price['usd'],
                    "coin": coin
                })
    
    print(f'[TRANSFORM] processed {len(rows)} coins')
    return pd.DataFrame(rows)
