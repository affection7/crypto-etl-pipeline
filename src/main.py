import logging

from pipelines.paprika import run_paprika_pipelines
from pipelines.gecko import run_gecko_pipelines
from pipelines.coinlore import run_coinlore_pipelines

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(filename)s | %(message)s')

if __name__ == "__main__":
    run_paprika_pipelines()
    run_gecko_pipelines()
    run_coinlore_pipelines()