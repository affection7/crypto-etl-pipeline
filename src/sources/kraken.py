import requests
from datetime import datetime
URL_kraken = "https://api.kraken.com/0/public/Spread?pair=BTC%2FUSD"

def extract_kraken(url: str):
    data = {}
    response = requests.get(url)
    data_kraken = response.json()
    data["kraken"] = data_kraken
    date = datetime.fromtimestamp(data["kraken"]["result"]["BTC/USD"][0][0])
    print(date)
    return data

extract_kraken(URL_kraken)