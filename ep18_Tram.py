'''Linear Kingdom has exactly one tram line. It has n stops, numbered from 1 to n in the order of tram's movement. At the i-th stop ai passengers exit the tram, while bi passengers enter it. The tram is empty before it arrives at the first stop. Also, when the tram arrives at the last stop, all passengers exit so that it becomes empty.

Your task is to calculate the tram's minimum capacity such that the number of people inside the tram at any time never exceeds this capacity. Note that at each stop all exiting passengers exit before any entering passenger enters the tram.'''


stops = int(input("Enter the number of stops"))
lst = list()
x = 0
c =0
m = list()
for i in range(stops):
    lst.append(input().split())
lst1 = list()
for k in range(stops):
    for j in range(2):
        lst1.append(lst[k][j])
for n in lst1:

    n = int(n)
    if c%2 == 0:
        n = -int(n)
    x = x + n
    c = c+1
    m.append(x)

print(max(m))
