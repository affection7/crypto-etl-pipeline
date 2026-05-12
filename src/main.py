import logging
from config import URL_GECKO, URL_PAPRIKA, HEADERS
from pipelines.paprika import run_paprika_pipelines
from pipelines.gecko import run_gecko_pipelines

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(filename)s | %(message)s')

if __name__ == "__main__":
    run_paprika_pipelines()
    run_gecko_pipelines()
    # logging.debug("[EXTRACT] start")
    # data = extract_price(URL_GECKO, HEADERS, URL_PAPRIKA)
    # logging.debug("[TRANSFORM] start")
    # data_df = transform_price(data)
    # logging.debug("[LOAD] start")
    # load_to(data_df)
    # logging.debug("[PIPELINE] done")
 