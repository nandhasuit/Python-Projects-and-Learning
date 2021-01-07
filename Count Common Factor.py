num = [input("Enter the Number ") for i in range(2)]
a = int(num[0])
b = int(num[1])

x = max(a,b)

count = 0
for i in range(1, x):
    if a%i == 0:
        if b%i == 0:
            print(i)
            count = count+1
print('Count = ', count)

