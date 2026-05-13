import pandas as pd
import logging
from datetime import datetime, timezone

def transform_price(data_list: dict):
    rows = []
    date = datetime.now(timezone.utc)

    for coin_name in data_list["data"]:
        rows.append({
            "date": date,
            "nameid": coin_name["nameid"],
            "price": coin_name["price_usd"],
            "percent_change_24h": coin_name["percent_change_24h"],
            "percent_change_7d": coin_name["percent_change_7d"],
            "market_cap_usd": coin_name["market_cap_usd"],
            "source": "coin lore"
        })
    
    logging.info(f'[TRANSFORM] processed {len(rows)} coins')
    return pd.DataFrame(rows)