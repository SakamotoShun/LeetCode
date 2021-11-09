# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        v = set()
        def dfs(Node):
            if not Node:
                return False
            i = k - Node.val
            if i in v:
                return True
            else:
                v.add(Node.val)
                return dfs(Node.left) or dfs(Node.right)
        return dfs(root)
    
