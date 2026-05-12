import logging
import pandas as pd
from datetime import datetime
from datetime import datetime, timezone

def transform_price(data_list: dict):
    rows = []
    date = datetime.now(timezone.utc)
    timestamp = data_list['result']['BTC/USD'][-1][0]
    
    print(data_list['result']['BTC/USD'][-1])

    rows.append({
        "date": datetime.fromtimestamp(timestamp),
        "price": round(float(data_list['result']['BTC/USD'][-1][1]),2),
        "coin":  'bitcoin',
        "source": "kraken"
    })
    
    print(f'[TRANSFORM] processed {len(rows)} coins')
    return pd.DataFrame(rows)