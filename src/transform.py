import pandas as pd
from datetime import datetime, timezone

def transform_price(data_list: dict):
    rows = []
    date = datetime.now(timezone.utc)

    for source, value in data_list.items():
        if source == 'paprika':
            rows.append({
                "date": date, 
                "price": round(value["quotes"]["USD"]["price"], 2), 
                "coin": value["symbol"]
            })
        elif source == 'gecko':
            for coin_name, price_info  in value.items():
                rows.append({
                    "date": date, 
                    "price": price_info['usd'],
                    "coin": coin_name
                })
    
    print(f'[TRANSFORM] processed {len(rows)} coins')
    return pd.DataFrame(rows)
