import os

filename = r"C:\Users\Imosh\Desktop\PP2\Lab_6\dir and files\copy_example.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} deleted")