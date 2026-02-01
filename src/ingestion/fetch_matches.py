import requests
import pandas as pd
from app.config.settings import OPENDOTA_BASE_URL
from app.db.duckdb import get_connection


def fetch_public_matches(limit=50):
    url = f"{OPENDOTA_BASE_URL}/publicMatches"
    params = {"limit": limit}

    response = requests.get(url, params=params)
    response.raise_for_status()

    return pd.DataFrame(response.json())


def save_matches(df: pd.DataFrame):
    con = get_connection()

    con.execute(
        """
        create table if not exists public_matches AS
        select
            *
        from
            df
        """
    )

    con.close()


if __name__ == "__main__":
    df = fetch_public_matches(50)
    save_matches(df)

    print("Dados salvos no DuckDB")
    print(df.head())
