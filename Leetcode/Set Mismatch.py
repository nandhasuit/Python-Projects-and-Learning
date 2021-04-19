nums = [1,2,2,4]
c = []
for i in range(len(nums)-1):
    if nums[i] >= nums[i+1]:
        c.append(nums[i])
        c.append(nums[i]+1)

print(set(nums))
