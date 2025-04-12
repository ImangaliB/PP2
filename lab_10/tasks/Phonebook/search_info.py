from info_database1 import *

def search_user(name=None, phone=None):
    conn = open_database()
    cur = conn.cursor()

    if name:
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    elif phone:
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    else:
        cur.execute("SELECT * FROM phonebook")

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    close_database()

search_user()  
print()                    
search_user(name="Дина")           
search_user(phone="12344")

mode = input("Іздеу түрі (name/phone/all): ")

if mode == "name":
    name = input("Іздейтін атыңыз: ")
    search_user(name=name)
elif mode == "phone":
    phone = input("Іздейтін нөміріңіз: ")
    search_user(phone=phone)
else:
    search_user()