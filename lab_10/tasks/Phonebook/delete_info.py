from info_database1 import *

def delete_user(identifier):
    conn = open_database()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM phonebook
        WHERE name = %s OR phone = %s
    """, (identifier, identifier))

    conn.commit()
    cur.close()
    close_database()
    print(f"'{identifier}' бойынша жазба өшірілді.")

delete_user("Gulvira")               
delete_user("87082823030")   

# name_or_phone = input("Кімді өшіргіңіз келеді (аты немесе номері)? ")
# delete_user(name_or_phone)  
