class arithnum:
    def enseq(self,m,k):
        c = ""
        h = list()
        for i in range(1,(k*m+1),m):
            h.append(i)
        y = list()
        for w in range(1,(len(h)+1)):
            t = int(input('enter the value :'))
            y.append(t)
        p = 0
        while True:
            if h[p] != y[p]:
                print(y[p])
                break
            p = p+1

m = int(input('enter the diff'))
k = int(input('enter the count:'))
a = arithnum()
a.enseq(m,k)