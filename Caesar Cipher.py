str1 ='abc'
n = 4
a= 'abcdefghijklmnopqrstuvwxyz'
c=""
m = 0
#going through length of the given letters
for i in range(len(str1)):
    #going through length of alphabets
    for j in range(len(a)):
        #compareing given str with each alphabets
        if str1[i] == a[j]:
            #if yes checking position of the letter id greater then 26 or less, if so add them and give the position
            #or else if the position is grater, add the position and subtract it with 26 
            if (j+n) <= 26:
                m = j+n
            elif (j+n) >= 26:
                m= j+n-26
            c = c+a [m]
print(c)



