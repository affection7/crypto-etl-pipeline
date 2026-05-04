import requests

from dotenv import load_dotenv

load_dotenv()

def extract_price(url_gecko: str, headers_gecko: dict, url_paprika: str):
    response_bes = requests.get(url_gecko, headers=headers_gecko)
    data_bes = response_bes.json()
    
    response_ton = requests.get(url_paprika)
    data_ton = response_ton.json()
    
    data = [data_bes, data_ton] 
    
    print(f"[EXTRACT] done. Collected {len(data)} items")
    return data