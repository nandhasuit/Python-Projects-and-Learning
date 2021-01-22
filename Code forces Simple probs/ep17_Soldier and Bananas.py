'''A soldier wants to buy w bananas in the shop. He has to pay k dollars for the first banana, 2k dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana).

He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?'''


print('The cost of the first banana, initial number of dollars the soldier has and number of bananas he wants')
cost, Money, bananas = [int(input('')) for i in range(3)]
k = 0
for i in range(1, bananas+1):
    k = k + i*cost
M = k - Money
print(M)

