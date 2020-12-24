
class solution:
    def commonpref(strs):
        if len(strs) == 0:
            return ''
        if len(strs)== 1:
            return strs[0]
        pref = strs[0]
        plen = len(pref)
        for s in strs[1:]:
            while pref  != s[0:plen]:
                pref = pref[0:(plen-1)]
                plen = plen-1
        return pref

num = input('enter the number of iteration')
strs = list()
for i in range(int(num)):
    words = input('Enter the words')
    strs.append(words)

pl = solution.commonpref(strs)
print(pl)


