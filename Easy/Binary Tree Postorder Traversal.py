ans = []
def ordered(node, ans):
    if node.left:
        ordered(node.left, ans)
    if node.right:
        ordered(node.right, ans)
    ans.append(node.val)
if not root: return ans
ordered(root, ans)
return ans