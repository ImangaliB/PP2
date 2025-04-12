import psycopg2

conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = "1234",
    host = "localhost",
    port = "5432"
)
conn.autocommit = True
cur = conn.cursor()

cur.execute("SELECT 1 FROM pg_database WHERE datname = 'snake_game'")
exists = cur.fetchone()
if not exists:
    cur.execute("CREATE DATABASE snake_game")
    print("База жасалды: snake_game")
else:
    print("База бұрыннан бар")

cur.close()
conn.close()

