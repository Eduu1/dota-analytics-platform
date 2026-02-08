from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

DB_PATH = DATA_DIR / "dota.duckdb"

OPENDOTA_BASE_URL = "https://api.opendota.com/api"
