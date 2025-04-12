from info_database1 import *
from print_database import *


conn = open_database()
cur = conn.cursor()

name = input("What is your name?  ")
phone = input("What is your phone number?   ")

cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s,%s)",(name,phone))
conn.commit()
print(f"Datas is insert: {name} - {phone}")


print_database()

cur.close()
close_database()