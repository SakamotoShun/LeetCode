ans : []
if root:
    ans.append(root.val)
    preorderTraversal(root.left)
    preorderTraversal(root.right)
    return ans