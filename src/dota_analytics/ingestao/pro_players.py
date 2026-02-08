import requests
import pandas as pd
from dota_analytics.config.config import OPENDOTA_BASE_URL
from dota_analytics.db.duckdb import get_conexao


def encontrar_pro_players():
    url = f"{OPENDOTA_BASE_URL}/proPlayers"
    r = requests.get(url)
    r.raise_for_status()
    return pd.DataFrame(r.json())


def salvar_pro_players(df: pd.DataFrame):
    con = get_conexao()
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS bronze_pro_players AS 
        SELECT * FROM df
        """
    )
    con.close()


if __name__ == "__main__":
    df = encontrar_pro_players()
    salvar_pro_players(df)
    print(df.head())
