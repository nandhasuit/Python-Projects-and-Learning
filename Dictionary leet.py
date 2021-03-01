words = ["k", "lg", "it", "oidd", "oid", "oiddm", "kfk", "y", "mw", "kf", "l", "o", "mwaqz", "oi", "ych", "m", "mwa"]
result = []
k = ""
for word in words:
    i = len(word) - 1
    flag = 1
    while i >= 1:
        if word[:i] not in words:
            flag = 0
            break
        i -= 1
    if flag:
        if (len(word) > len(k)) or (len(word) == len(k) and word < k):
            k = word
print(k)

