from app.db.duckdb import get_connection

con = get_connection()

query = con.execute(
    """ 
    select
        COUNT(*) AS total_matches,
        AVG(avg_rank_tier) AS avg_rank_tier
    from
        public_matches
    """
).fetchdf()

print(con.execute("Show tables").fetch_df())
print(con.execute("describe public_matches").fetch_df())


print(query)
con.close()
