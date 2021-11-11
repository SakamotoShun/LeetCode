# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

#     a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

def check(node):
    if not node:
        return 0
    curr = 1
    left = check(node.left)
    right = check(node.right)
    if left < 0 or right < 0:
        return -1
    if (left - right) > 1:
        return -1
    return curr + max(left, right)

if check(root) < 0:
    return False
else: return True