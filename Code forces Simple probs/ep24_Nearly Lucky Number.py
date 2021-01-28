'''Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Unfortunately, not all numbers are lucky. Petya calls a number nearly lucky if the number of lucky digits in it is a lucky number. He wonders whether number n is a nearly lucky number.'''

num = str(input('enter the number'))
f = False
for i in range(len(num)):
    if num[i] == '7' or num[i] == '4':
        f = True
    else:
        f = False
        break

if f == True:
    print('Yes')
else:
    print('No')


