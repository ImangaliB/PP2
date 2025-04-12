from info_database2 import *

def get_or_create_user(username):
    conn = open_database()
    cur = conn.cursor()

    
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
        print(f"Welcome, {username}!")
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        print(f"Insert new player: {username}")

    conn.commit()
    cur.close()
    close_database()

    return user_id
