import math
num = int(input('enter the number of positive integer'))
posnum = list()
for i in range(num):
    k = int(input('enter the possitive integer'))
    posnum.append(k)
l=0

for j in range(len(posnum)):
    l = posnum[j]
    if (math.pow(l,l))  == l*l:
        print('no')
    elif (math.pow(l,l))  != l*l:
        print('yes')