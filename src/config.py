import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL_GECKO  = os.getenv("URL_GECKO")
URL_PAPRIKA = os.getenv("URL_PAPRIKA")
DB_PASS = os.getenv("DB_PASS")