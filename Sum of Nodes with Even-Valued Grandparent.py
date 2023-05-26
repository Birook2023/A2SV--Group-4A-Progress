# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, vis):
            nonlocal res
            if not node:
                return
            vis.append(node.val)
            n = len(vis)
            if n > 2 and vis[n - 3] % 2 ==0:
                res += node.val
            dfs(node.left, vis[:])
            dfs(node.right, vis[:])
        res = 0
        dfs(root, [])
        return res
    
        
