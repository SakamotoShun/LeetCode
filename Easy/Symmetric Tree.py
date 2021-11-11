# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

root = [1,2,2,3,4,4,3]
# output = true

def check(left, right):
    if left is None or right is None:
        return left == right
    if left.val != right.val:
        return False
    return check(left.right, right.left) and check(left.left, right.right)
return check(root.left, root.right)