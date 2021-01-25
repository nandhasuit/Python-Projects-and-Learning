m = "hello"
'''Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word s.'''

def chatRoom():
    x = 0
    s = input()
    for i in range(len(s)):
        if s[i] == m[x]:
            x += 1
        if x == 5:
            return "YES"
    return "NO"


print(chatRoom())

