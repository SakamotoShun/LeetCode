# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

root = [3,9,20,null,null,15,7]
# output = 3



if not root:
    return 0
curr = [root]
depth = 0

while len(curr) > 0:
    depth += 1
    temp_curr = curr
    curr = []
    for node in temp_curr:
        if node.left:
            curr.append(node.left)
        if node.right:
            curr.append(node.right)
return depth