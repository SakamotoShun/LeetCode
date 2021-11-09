# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

nums = [1, 1, 2]

if len(nums) == 0: print('False')
if len(nums) == 1: print('True')

j = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i -1]:
        nums[j] = nums[i]
        j += 1
for k in range(i, j-1, -1):
    del nums[k]
print(j)
