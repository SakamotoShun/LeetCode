# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

input = [3,9,20,null,null,15,7]
# output: 2

temp = [(root, 1)]

if not root:return 0
for i, depth in temp:
    if i:
        if not i.right and not i.left:
            return depth
        if i.left:
            temp.append((i.left, depth + 1))
        if i.right:
            temp.append((i.right, depth + 1))
