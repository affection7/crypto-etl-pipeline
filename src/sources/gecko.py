import requests
import logging
from requests.exceptions import HTTPError

def extract_gecko(url: str, headers: dict):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        logging.info("[EXTRACT] gecko success")
        return data
    except HTTPError as http_gecko_error:
        logging.error(f"HTTP ощибка: {http_gecko_error}")