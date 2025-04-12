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

cur.execute("SELECT 1 FROM pg_database WHERE datname = 'phonebook_db'")
exists = cur.fetchone()
if not exists:
    cur.execute("CREATE DATABASE phonebook_db")
    print("База жасалды: phonebook_db")
else:
    print("База бұрыннан бар")

cur.close()
conn.close()

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(15)
    )
""")
conn.commit()


cur.close()
conn.close()