num = int(input('Enter the test case: '))

lst1 =[int(i) for i in range(num)]
for n in lst1:
    if n>=1 and n <= (10**9):
        prod = 1
        sum = 0
        for i in range(1,n+1):
            prod = prod * 1
            sum =sum + 1
        if prod % sum == 0:
            print('YEAH')
        else:
            print('nope')