import random

def getran(strlen):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    res = ""

    for i in range(strlen):
        res += alp[random.randrange(26)]
    return res

def score(goal,teststr):
    numsame = 0
    for i in range(len(goal)):
        if goal[i] == teststr[i]:
            numsame += 1
    return numsame/len(goal)

def main():
    goalstr = 'a computer science portal for geeks'
    teststr = getran(35)
    best = 0
    newsc = score(goalstr, teststr)
    B = 0
    while newsc <1:
        if newsc > B:
            print(teststr)
            B  =  newsc
        teststr = getran(35)
        newsc = score(goalstr, teststr)\

main()




