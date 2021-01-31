'''Anton likes to play chess, and so does his friend Danik.

Once they have played n games in a row. For each game it's known who was the winner — Anton or Danik. None of the games ended with a tie.

Now Anton wonders, who won more games, he or Danik? Help him determine this.

Input
The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — the number of games played.

The second line contains a string s, consisting of n uppercase English letters 'A' and 'D' — the outcome of each of the games. The i-th character of the string is equal to 'A' if the Anton won the i-th game and 'D' if Danik won the i-th game.'''


num = int(input("Enter the number of games: "))
strs = input("Enter the string: ")
c = 0
for i in range(num):
    if strs[i] == 'A':
        c = c+1

if c > (num/2):
    print("Anton ")
elif c == (num/2):
    print("Friends")
elif c < (num/2):
    print("Danik ")




