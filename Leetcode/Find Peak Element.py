nums = [1,2]

for i in range(len(nums)-1):
    j = i-1
    if nums[i] > nums[j]:
        if not nums[i+1]:
            print(nums[i])
        if nums[i] > nums[i+1]:
            print(nums[i])




