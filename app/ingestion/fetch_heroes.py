import requests
import pandas as pd
from app.config.settings import OPENDOTA_BASE_URL
from app.db.duckdb import get_connection


def fetch_heroes():
    url = f"{OPENDOTA_BASE_URL}/heroes"
    response = requests.get(url)
    response.raise_for_status()
    return pd.DataFrame(response.json())



def save_heroes(df: pd.DataFrame):
    con = get_connection()

    con.execute(
        """
        CREATE TABLE IF NOT EXISTS dim_heroes AS
        SELECT * FROM df
        """
    )
    con.close()

if __name__ == "__main__":
    df = fetch_heroes()
    save_heroes(df)
    print("Herois salvos!")