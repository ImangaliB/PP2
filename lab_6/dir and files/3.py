import os


path = r"C:\Users\Imosh\Desktop\PP2\Lab_6\dir and files\example.txt"


if os.path.exists(path):
    print("Filename:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("Path does not exist")