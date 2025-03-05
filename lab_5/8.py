import re

with open(r"C:\Users\Imosh\Desktop\PP2\Lab_5\regex\row.txt", encoding="utf-8") as f:
    text = f.read()


matches = re.split(r"(?=[A-Z])", text)
print(matches)