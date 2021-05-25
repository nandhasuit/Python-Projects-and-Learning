def removeDuplicates(nums):
    i =0
    c = 0
    lenn =(len(nums)-1)
    while i< lenn:
        j = i+1
        while j< len(nums) and nums[i] == nums[j]:
            nums.remove(nums[j])

        i = i+1
    return nums


i = 0
c = 0
lenn = (len(nums) - 1)
while i < lenn:
    j = i + 1
    while j < (len(nums) - 1) and nums[i] >= nums[j]:
        j = j + 1
    if nums[i] < nums[j]:
        nums[i + 1] = nums[j]
    i = i + 1
for k in range(len(nums) - 1):
    if nums[k] < nums[k + 1]:
        c = c + 1
    else:
        break

for i in range(c):
    nums.re



if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))