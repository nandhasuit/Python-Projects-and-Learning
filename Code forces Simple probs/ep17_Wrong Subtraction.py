'''Little girl Tanya is learning how to decrease a number by one, but she does it wrong with a number consisting of two or more digits. Tanya subtracts one from a number by the following algorithm:

if the last digit of the number is non-zero, she decreases the number by one;
if the last digit of the number is zero, she divides the number by 10 (i.e. removes the last digit).
You are given an integer number n. Tanya will subtract one from it k times. Your task is to print the result after all k subtractions.

It is guaranteed that the result will be positive integer number.'''

print('Enter the number to be sub and nuber of subractions')
n, k = [int(input()) for i in range(2)]

for i in range(k):
    if n%10 != 0:
        n = n-1
    elif n%10 == 0:
        n = n/10

print(int(n))
