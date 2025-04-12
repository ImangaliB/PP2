from info_database2 import *

def get_latest_level(user_id):
    conn = open_database()
    cur = conn.cursor()

    cur.execute("""
        SELECT level FROM user_scores
        WHERE user_id = %s
        ORDER BY created_at DESC
        LIMIT 1
    """, (user_id,))

    row = cur.fetchone()

    cur.close()
    close_database()

    return row[0] if row else 1
