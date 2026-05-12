import requests

URL_kraken = "https://api.kraken.com/0/public/Spread?pair=BTC%2FUSD"

def extract_kraken(url: str) -> list[dict]:
    response = requests.get(url)
    response.raise_for_status()
    data_kraken = response.json()
    print(data_kraken['result']['BTC/USD'][-1])
    return data_kraken
