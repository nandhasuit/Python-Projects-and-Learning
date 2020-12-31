str1 ='abc'
n = 4
a= 'abcdefghijklmnopqrstuvwxyz'
c=""
m = 0
for i in range(len(str1)):
    for j in range(len(a)):
        if str1[i] == a[j]:
            if (j+n) <= 26:
                m = j+n
            elif (j+n) >= 26:
                m= j+n-26
            c = c+a [m]
print(c)



