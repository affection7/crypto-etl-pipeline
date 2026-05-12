import pandas as pd
import logging
from datetime import datetime, timezone

def transform_price(data_list: dict):
    rows = []
    date = datetime.now(timezone.utc)

    rows.append({
        "date": date,
        "price": round(float(data_list["quotes"]["USD"]["price"]),3),
        "coin": data_list["name"].lower(),
        "source": "paprika",

    })

    print(f'[TRANSFORM] processed {len(rows)} coins {rows}')
    return pd.DataFrame(rows)
