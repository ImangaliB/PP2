from info_database2 import *

def print_database():
    conn = open_database()
    cur = conn.cursor()

    cur.execute("SELECT * FROM user_scores;")
    table = cur.fetchall()
    for row in table:
        print(row)

    cur.execute("SELECT * FROM users;")
    table = cur.fetchall()
    for row in table:
        print(row)

    cur.close()
    close_database()

print_database()
