x = input()


up = 0

down = 0


for i in x:
    if i.isupper():
        up += 1
    else:
        down += 1

print(f"Number of upppercases: {up}, number of lowercases: {down}" )