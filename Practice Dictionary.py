#Ascending and Decending
'''
import random

a =dict()

for i in range(1,20,3):
    b = input('Enter the name: ')
    a[i] = b
d = list(a.items())
random.shuffle(d)
m = dict(d)

while True:
    ask = input('For Ascending type A, For Descending type D: ')
    if ask == 'A':
        k = sorted(m.items())
        print(k)
        break
    elif ask == 'D':
        k =sorted(m.items(), reverse=True)
        print(k)
        break
    else:
        print('Enter the mentioned order to print')
        continue'''

#Adding a key
'''
a = {0: 10, 1: 20}
a[2] = 30
print(a)'''

#Concat Dic
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic ={}

for i in (dic1,dic2,dic3):dic.update(i)
print(dic)'''

#Check give key exist
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic ={}
for i in (dic1,dic2,dic3):dic.update(i)

a = int(input('enter the key you need to find: '))

for i in dic:
    if a == i:
        print('The key already exist')
        break
    continue'''
#iterate dictionary
'''class  iterate():

    def dic(self, a):
        for i,j in a.items():
           print(i,j)

a= {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

c =iterate()
c.dic(a)'''










