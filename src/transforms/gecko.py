import pandas as pd
import logging
from datetime import datetime, timezone

def transform_price(data_list: dict):
    rows = []
    date = datetime.now(timezone.utc)

    for coin_name, coin_info in data_list.items():
        rows.append({
            "date": date, 
            "price": coin_info['usd'],
            "coin": coin_name,
            "source": "gecko"
        })
    
    logging.info(f'[TRANSFORM] processed {len(rows)} coins')
    return pd.DataFrame(rows)