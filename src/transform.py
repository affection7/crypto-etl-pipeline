import pandas as pd
from datetime import datetime, timezone

def transform_price(data: dict):
    rows = []
    date = datetime.now(timezone.utc)
    
    print("[TRANSFORM] start")
    for coin, price in data.items():
        rows.append({"date": date, "price": price['usd'], "coin": coin})
    print(f'[TRANSFORM] processed {len(data.items())} coins')
    return pd.DataFrame(rows)