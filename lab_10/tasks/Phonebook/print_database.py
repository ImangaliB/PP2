from info_database1 import *

def print_database():
    conn = open_database()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook;")
    table = cur.fetchall()
    for row in table:
        print(row)

    cur.close()
    close_database()

print_database()
