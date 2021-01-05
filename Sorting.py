#bubble sort
'''
count = int(input('Enter the range oof list: '))
fh = [input("Enter the List of numbers: ") for i in range(count)]




for i in range(len(fh)):
    for j in range(len(fh)):
        if fh[j] < fh[i]:
            temp = fh[i]
            fh[i] =fh[j]
            fh[j] = temp

print(fh)'''

#selection sort
'''count = int(input('Enter the range oof list: '))
fh = [int(input("Enter the List of numbers: ")) for i in range(count)]

for i in range(len(fh)):
    mini = i
    for j in range(i+1, len(fh)):
        if fh[mini] > fh[j]:
            mini = j
    fh[mini], fh[i] = fh[i], fh[mini]


print(fh)'''








