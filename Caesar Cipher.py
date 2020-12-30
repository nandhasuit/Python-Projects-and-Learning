str1 ='xyz'
n = 4
a= 'abcdefghijklmnopqrstuvwxyz'
c=""
for i in range(len(str1)):
    for j in range(len(a)):
        if str1[i] == a[j]:
            m = j+n
            c = c+a[m]
print(c)



