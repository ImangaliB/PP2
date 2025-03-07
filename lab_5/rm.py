import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.search(r"\s", txt)  


print("The first white-space character is located in position:", x.start())


import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.split(r"\s", txt, maxsplit=1)
print(x)


import re

txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt, count=2)
print(x)


import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())