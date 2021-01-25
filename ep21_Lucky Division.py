'''Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya calls a number almost lucky if it could be evenly divided by some lucky number. Help him find out if the given number n is almost lucky.'''

num = input('Enter the number')
m =len(num)
f = 0
n = int(num)
if n%7 == 0 or n%4 == 0:
    print('YES')
else:
    for i in range(m):
        if n%10 == 7 or n%10 == 4:
            f = f+1
        n = int(n/10)



    if f == m:
        print('YES')
    else:
        print('NO')
