from info_database2 import *

def save_score(user_id,username, score, level):
    conn = open_database()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_scores (user_id, username, score, level)
        VALUES (%s,%s, %s, %s)
    """, (user_id,username, score, level))

    conn.commit()
    cur.close()
    close_database()
    print(f"Ұпай ({score}) және деңгей ({level}) базаға сақталды.")
