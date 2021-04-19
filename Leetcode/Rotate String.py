A = 'abcde'
B = 'cdeab'
c = ""
f = 0
for i in B:
    B = B[1:]+ B[0]
    if A == B:
        f = 1
        break
if f == 1:
    print(True)
else:
    print(False)




