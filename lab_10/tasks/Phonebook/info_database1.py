import psycopg2

conn1 = None
cur = None

def open_database():
    global conn1
    conn1 = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="Imosh_07",
    host="localhost",
    port="5432"
    )
    return conn1
    
def close_database():
    global conn1
    if conn1:
        conn1.close()