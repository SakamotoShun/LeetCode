# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

if root:
    targetSum -= root.val
    if targetSum == 0 and (not root.left and not root.right):
        return True
    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
return False