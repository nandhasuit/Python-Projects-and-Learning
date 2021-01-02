import string
str1 = input("enter the string: ")
k  =len(str1)
if k > 4 and k < 25:
    if type(str1[0]) == str:
        if str1 == str or str1 == int:
            print(yes)
