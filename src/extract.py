import requests
import logging

from dotenv import load_dotenv
from requests.exceptions import HTTPError

load_dotenv()

def extract_price(url_gecko: str, headers_gecko: dict, url_paprika: str):
    data = {}
    try:
        response_bes = requests.get(url_gecko, headers=headers_gecko, timeout=10)
        response_bes.raise_for_status()
        data_bes = response_bes.json()
        data["gecko"] = data_bes 
        logging.info("[EXTRACT] gecko success")
    except HTTPError as http_gecko_error:
        logging.error(f"HTTP ощибка: {http_gecko_error}")
        
    try:
        response_ton = requests.get(url_paprika, timeout=10)
        response_ton.raise_for_status()
        data_ton = response_ton.json()
        data["paprika"] = data_ton
        logging.info("[EXTRACT] paprika success")
    except HTTPError as http_paprika_error:
        logging.error(f"HTTP ощибка: {http_paprika_error}")
        
    if len(data) == 0:
        logging.error("FATAL ERROR")
    logging.info(f"[EXTRACT] done. Collected {len(data)} items")
    return data