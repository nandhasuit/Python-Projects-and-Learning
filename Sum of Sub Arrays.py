class subarray:
    def sumarray(self,x,n,k):
        li = list()
        re = 0
        i = 0
        while i < n:
            f = 0
            c = 0
            while i<n and int(x[i]) <= k:
                li.append(x[i])
                c = c+1
                if int(x[i]) == k:
                    f = 1
                i = i + 1
            if f == 1:
                re = re +c

            while i<n and int(x[i]) > k:
                i = i + 1
        print(re)


x = [2, 1, 4, 9, 2, 3, 8, 3, 4]
n = len(x)
k = 4
l = subarray()
l.sumarray(x,n,k)
