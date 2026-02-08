import duckdb
from dota_analytics.config.config import DB_PATH


def get_conexao():
    return duckdb.connect(DB_PATH)
