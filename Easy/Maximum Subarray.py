# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

nums = [-2,1,-3,4,-1,2,1,-5,4]

arr = [0 for i in range(len(nums))]
arr[0] = nums[0]
for i in range(1, len(nums)):
    arr[i] = max(arr[i-1]+ nums[i], nums[i])
print(max(arr))