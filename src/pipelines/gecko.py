from sources.gecko import extract_gecko
from transforms.gecko import transform_price
from loaders.load import load_to
from config import URL_GECKO, HEADERS

def run_gecko_pipelines():
    data = extract_gecko(URL_GECKO, HEADERS)
    data_clean = transform_price(data)
    load_to(data_clean)