import duckdb
from pathlib import Path

DB_PATH = Path("data/dota.duckdb")


def get_connection():
    return duckdb.connect(DB_PATH)
