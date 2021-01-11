class stock:

    def stoc(self,lst,days,b):
        i = 1
        f =0
        k = list()
        while i < days:
            while i < days and lst[b] <= lst[i]:
                if lst[b] == lst[i]:
                    f = 1
                if f == 1:
                    k.append((lst[b] - lst[i]))
                    i = i+1
            while i < days and lst[b] > lst[i]:
                i = i+1
        print(max(k))


#days = int(input('Enter the nummber of days: '))
#stocks = [int(input('Enter the stocks rate: ')) for i in range(1,days)]
#b= int(input('enter the day you want to buy'))
days = 7
stocks = [100, 180, 260, 310, 40, 535, 695]
b = 4
n = stock()
n.stoc(stocks,days,b)











