import requests

from dotenv import load_dotenv

load_dotenv()

def extract_price(url_bes: str, url_ton: str):
    response_bes = requests.get(url_bes)
    data_bes = response_bes.json()
    
    response_ton = requests.get(url_ton)
    data_ton = response_ton.json()
    
    data = [data_bes, data_ton] 
    
    print(f"[EXTRACT] done. Collected {len(data)} items")
    return data