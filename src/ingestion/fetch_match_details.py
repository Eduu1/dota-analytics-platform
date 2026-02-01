import requests
from app.config.settings import OPENDOTA_BASE_URL


def fetch_match_details(match_id: int):
    url = f"{OPENDOTA_BASE_URL}/matches/{match_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
