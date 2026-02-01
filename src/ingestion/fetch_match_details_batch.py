import time
from app.db.duckdb import get_connection
from app.ingestion.fetch_match_details import fetch_match_details


def get_match_ids(limit=20):
    con = get_connection()
    df = con.execute(
        """
        SELECT match_id
        FROM public_matches
        ORDER BY start_time DESC
        LIMIT ?
        """,
        [limit],
    ).fetchdf()
    con.close()
    return df["match_id"].tolist()


def run_batch(limit=20, sleep=1):
    match_ids = get_match_ids(limit)

    for match_id in match_ids:
        try:
            print(f"Fetching match {match_id}")
            data = fetch_match_details(match_id)

            # por enquanto só printa
            print(data["match_id"], "OK")

            time.sleep(sleep)  # respeita a API

        except Exception as e:
            print(f"Erro no match {match_id}: {e}")


if __name__ == "__main__":
    run_batch(limit=10)
