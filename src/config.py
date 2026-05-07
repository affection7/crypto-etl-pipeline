import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
HEADERS = {"x-cg-api-key": API_KEY}
URL_GECKO  = os.getenv("URL_GECKO")
URL_PAPRIKA = os.getenv("URL_PAPRIKA")
DB_PASS = os.getenv("DB_PASS")
DB_URL = f"postgresql://neondb_owner:{DB_PASS}@ep-shiny-firefly-ah7am9sh-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&connect_timeout=10"