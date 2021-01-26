nums = input()
k = len(str(nums))
lst =list()
for i in range(k):
    if int(nums[i]) not in lst:
        lst.append(int(nums[i]))
print( sorted(lst))


