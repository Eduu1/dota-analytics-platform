import requests
import pandas as pd
from dota_analytics.config.config import OPENDOTA_BASE_URL
from dota_analytics.db.duckdb import get_conexao


def encontrar_public_matches(limit=100):
    url = f"{OPENDOTA_BASE_URL}/publicMatches"
    r = requests.get(url)
    r.raise_for_status()
    return pd.DataFrame(r.json())


def salvar_public_matches(df: pd.DataFrame):
    con = get_conexao()
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS bronze_public_matches AS 
        SELECT * FROM df
        """
    )
    con.close()


if __name__ == "__main__":
    df = encontrar_public_matches(limit=100)
    salvar_public_matches(df)
    print(df.head())
