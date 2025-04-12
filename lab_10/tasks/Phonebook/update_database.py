from info_database1 import *
from print_database import *

def update_user(old_name, new_name=None, new_phone=None):
    conn = open_database()
    cur = conn.cursor()

    if new_name and new_phone:
        cur.execute("UPDATE phonebook SET name = %s, phone = %s WHERE name = %s",
                    (new_name, new_phone, old_name))
    elif new_name:
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s",
                    (new_name, old_name))
    elif new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s",
                    (new_phone, old_name))
    else:
        print("Ешқандай өзгеріс енгізілген жоқ.")

    conn.commit()
    cur.close()
    close_database()
    print(f"'{old_name}' атты қолданушы жаңартылды.")

update_user("Nurik",new_name="Almaz")
update_user("wer", new_phone="12344")
update_user("esfrd", new_name="Дина", new_phone="87015556677")

