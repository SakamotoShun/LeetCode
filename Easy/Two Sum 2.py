nums = [2,7,11,15]
target = 9
# Output: [1,2]
# Output: Because nums[1] + nums[2] == 9, we return [1, 2].

total = None
i = 0
j = len(nums) - 1

while nums[i] + nums[j] != target:
    if target > nums[i] + nums[j]:
        i += 1
    else:
        j -= 1
print([i+1, j+1])