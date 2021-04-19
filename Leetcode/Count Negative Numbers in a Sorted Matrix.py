grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
c = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] < 0:
            c = c+1
print(c)