import re

text = input()
to_find = input()

ptrn = re.compile(to_find+".*")

print(re.findall(ptrn, text)[0])
