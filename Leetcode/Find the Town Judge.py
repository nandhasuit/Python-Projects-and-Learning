trust = [[1,2]]
N = 2
c = []
for j in range(1,N+1):
    for i in range(len(trust)):
        if j == trust[i][0]:
            if trust[i][0] not in c:
                c.append(trust[i][0])
for i in range(1,N+1):
    if i not in c:
        print(i)
    else:
        print(-1)
