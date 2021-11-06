nums = [4,7,11,2]
target = 9
# Output: [1,3]
# Output: Because nums[1] + nums[3] == 9, we return [1, 3].

i = 0
j = 1
total = None

while True:
    total = nums[i] + nums[j]
    if total != target:
        if j == len(nums) - 1:
            i += 1
            j = i + 1
        else:
            j += 1
    else:
        print([i, j])
        break
