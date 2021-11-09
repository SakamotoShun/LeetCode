# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

nums = [3,2,2,3]
val = 3

i = 0
j = len(nums)
while i < j:
    if nums[i] == val:
        nums[i] = nums[j-1]
        j -= 1
    else:
        i += 1
print(j)
        