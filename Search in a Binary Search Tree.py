# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        currNode = root
        while currNode:
            if val > currNode.val:
                currNode = currNode.right
            elif val < currNode.val:
                currNode = currNode.left
            else:
                return currNode
        

        

            
