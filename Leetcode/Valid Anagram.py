s = "anagram"
t = "negaram"
lt =[i for i in t]

for i in s:
    if i in lt:
        lt.remove(i)

if lt == []:
    print(True)
else:
    print(False)