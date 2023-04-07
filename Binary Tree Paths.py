# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = "" 
        
        def binarypath(node, path):
            if node is None:
                return []
            path += str(node.val)
            if node.left is None and node.right is None:
                res.append(path)
            else:
              binarypath(node.left, path + "->")
            
              binarypath(node.right, path + "->")
            
        binarypath(root, path)
        return res
