#divisible by 7 and multiple of 5
'''start =1500
end = 2700
lst = list()
for i in range(start, end+1):
    if i%7==0 and i%5 == 0:
        lst.append(i)
print(lst)'''


#celsius fahrenheit

'''mode = str(input('enter the temperature mode to be converted as Celsius and Fahrenheit : '))
while True:
    if mode == 'Celsius':
        f= int(input('enter the fahrenhiet : ' ))
        c = (f-(32/9)*5)
        print(c)
        break
    elif mode == 'Fahrenheit':
        c= int(input('enter the celcious: '))
        f = (c/5)+(32/9)
        print(f)
        break
    else:
        print('enter the correct temperature mode')
        continue'''

#Random numbers
'''import random

while True:
    guess = int(input('enter the guessed number between 1 to 9: '))
    ran = random.randint(1,9)
    print(ran)
    if ran == guess:
        print('well guessed')
        break
    else:
        print('enter the guess again')
        continue'''

#pattern
'''t = 6
for i in range(t):
    for j in range(i):
        print('*', end="")
    print('\r')

for x in range (t):
    for y in range(t-x):
        print('*',end="")
    print('\r')'''
#reverse

'''
get= str(input('enter the words'))
a = ""
for i in get:
    a = i+a
print(a)'''

#datalist
'''
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in datalist:
    print (type(i))'''


#continue statement
'''
for i in range(10):
    if i%3 == 0:continue
    print(i)'''

#Fibonacci
'''
a = 0
b = 1
c= 0
print(0)
print(1)
for i in range(10):
    a = b + c
    c = b
    b = a
    print(a)'''

#Multiples
'''
for i in range(1, 50):
    if i%3 == 0:
        print('fizz')
    elif i%5 == 0:
        print('buzz')
    elif i%3==0 and i%5 == 0:
        print('fizzbuzz')
    else:
        print(i)'''

#matrix
'''
rows = 3
columns = 4
mul_lst = [[0 for col in range(columns)] for row in range(rows)]
for i in range(rows):
    for j in range(columns):
        mul_lst[i][j] = i*j

print(mul_lst)''




















