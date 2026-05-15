import requests
import logging
from requests.exceptions import HTTPError

def extract_paprika(url: str) -> dict:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        logging.info("[EXTRACT] paprika success")
        return data
    except HTTPError as http_paprika_error:
        logging.error(f"HTTP ошибка: {http_paprika_error}")
        raise


