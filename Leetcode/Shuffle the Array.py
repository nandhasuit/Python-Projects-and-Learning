s = [2,5,1,3,4,7]
ls = int(len(s)/2)
n = ls
a = 0
m = []

while ls>0:
        m.append(s[a])
        a = a+1
        m.append(s[n])
        n = n+1
        ls = ls-1
print(m)
