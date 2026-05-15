import requests
import logging
from requests.exceptions import HTTPError

def extract_coinlore(URL: str):
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        data_lore = response.json()
        logging.info("[EXTRACT] coin lore success")
        return data_lore
    except HTTPError as http_gecko_error:
        logging.error(f"HTTP ошибка: {http_gecko_error}")
        raise


# def transfor_lore(data: dict):
#     columns = ['name', 'rank', 'price_usd', 'percent_change_24h', 'market_cap_usd']
#     df = pd.DataFrame(data["coin_lore"]["data"])

#     df = df[columns].copy()
    
#     df['date'] = datetime.now(timezone.utc)
    
#     return df

# def loads(data: pd.DataFrame):
#     rows = data.values.tolist()
#     sql = 'INSERT INTO row.coin_lore (name, rank, price_usd, percent_change_24h, market_cap_usd, date) VALUES %s'
#     with psycopg2.connect(DATABASE_URL) as conn:
#         with conn.cursor() as cur:
#             execute_values(cur, sql, rows)
#             logging.info(f'[LOAD] rows prepared: {len(rows)}')
# clean_df = transfor_lore(load_coin_lore(URL))
# loads(clean_df)