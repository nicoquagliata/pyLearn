#file manager chapter
import re
archivo = open("sample.txt", encoding="utf-8")
informacion = archivo.read()
archivo.close()

print(informacion)

print(re.match(r"abcdefghijklmnopqrstuvwxyz",informacion))
print(re.match(r"abcdefghijk4qrstuvwxyz",informacion))

print(re.search(r"0123456789",informacion))
