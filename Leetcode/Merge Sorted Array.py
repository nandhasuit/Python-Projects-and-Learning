nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
n = 3
m =3
j=0
for i in range(len(nums1)):
    if nums1[i] == 0:
        nums1[i] = nums2[j]
        j=j+1
#[1,8,5,2,6,7]
for k in range(len(nums1)):
    m = nums1[k]
    j =k-1
    while j>= 0 and m <= nums1[j]:
        nums1[j+1] = nums1[j]
        j = j -1
    nums1[j+1] = m
print(nums1)

