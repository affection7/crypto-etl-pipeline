import pandas as pd
import logging

def validate_prices_df(df: pd.DataFrame):
    try:
        if df.empty:
            logging.info("[LOAD] No rows to load!!!")
            return False
        cols = {"date", "price", "coin", "source"}
        if cols ==  set(df.columns):
            return True
        else:
            logging.warning(f"Unexpected columns: {df.columns}")
            return False
    except Exception  as e:
        logging.error(e)
        return False