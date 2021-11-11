# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

p = [1,2,3]
q = [1,2,3]
# output = True

if p is None and q is None:
    return True
elif p is None or q is None:
    return False

return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)