import sqlite3 as sql
import pandas as pd

# Connect to the SQLite database
conn = sql.connect('../input/basketball/basketball.sqlite')

# Run a query and load it into a Pandas DataFrame
df_games = pd.read_sql_query("SELECT * FROM game", conn)

# Close the database connection
conn.close()

# Display the first few rows
print(df_games.head())

print("smile")