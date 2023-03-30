# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        self.insert(root, val)
        return root
        
    def insert(self, root, value):
        
        if value < root.val:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                self.insert(root.left, value)
        else:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                self.insert(root.right, value)
