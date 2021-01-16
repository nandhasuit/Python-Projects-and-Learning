
class solution:
#Defineing Object with string strs
    def commonpref(strs):
#return no prefix if len(strs) is 0 
        if len(strs) == 0:        
            return ''
#return strs[0] as prefix since onely one character is specified
        if len(strs)== 1:
            return strs[0]
#setting prefix is strs[0]
        pref = strs[0]
#plen as length of prefix
        plen = len(pref)
#iterating s from strs[1] since prefix is strs[0]     
        for s in strs[1:]:
#loop when pref != s[0 to len(prefix)]
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


