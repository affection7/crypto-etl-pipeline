import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
HEADERS = {"x-cg-api-key": API_KEY}

def extract_price(url: str):
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    return data