# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        update = root
        
        while update:
            if p.val > update.val and q.val > update.val:
                update = update.right
            elif p.val < update.val and q.val < update.val:
                update = update.left
            else:
                return update
