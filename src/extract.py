import requests

from dotenv import load_dotenv
from requests.exceptions import HTTPError

load_dotenv()

def extract_price(url_gecko: str, headers_gecko: dict, url_paprika: str):
    data = []
    try:
        response_bes = requests.get(url_gecko, headers=headers_gecko)
        response_bes.raise_for_status()
        data_bes = response_bes.json()
        data.append(data_bes)
    except HTTPError as http_gecko_error:
        print(f"HTTP ощибка: {http_gecko_error}")
        
    try:
        response_ton = requests.get(url_paprika)
        response_ton.raise_for_status()
        data_ton = response_ton.json()
        data.append(data_ton)
    except HTTPError as http_paprika_error:
        print(f"HTTP ощибка: {http_paprika_error}")
        
    if len(data) == 0:
        print("FATAL ERROR")
    print(f"[EXTRACT] done. Collected {len(data)} items")
    return data