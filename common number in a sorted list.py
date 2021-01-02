range1 = 2
range2 = int(input('enter the range of the list:' ))
lst = [[input('enter the  numbers: ') for i in range(range2)] for j in range(range1) ]

lst1 ,lst2 = lst[0] , lst[1]

for k in lst1:
    temp = k
    for j in lst2:
        if k == j:
            print(k)
            break
