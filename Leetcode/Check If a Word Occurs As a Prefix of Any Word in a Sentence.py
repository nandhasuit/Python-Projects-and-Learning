s = "i a nandha"
se = "nand"
s= s.split()
c = []
for i in range(len(s)):
    if se in s[i]:
        for j in range(len(se)):
            if se[j] != s[i][j]:
                c.append(-1)
                break
            else:
                c.append(i+1)
print(min(c))




