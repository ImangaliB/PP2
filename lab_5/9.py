import re

with open(r"C:\Users\Imosh\Desktop\PP2\Lab_5\regex\row.txt", encoding="utf-8") as f:
    text = f.read()


modified_text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
print(modified_text)