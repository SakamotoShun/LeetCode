# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

nums = [-10,-3,0,5,9]
length = len(nums)

if length == 0:
    return None

i = length//2
balanced = TreeNode(nums[i], left = self.sortedArrayToBST(nums[0:i])   , right = self.sortedArrayToBST(nums[i+1:]))

return balanced