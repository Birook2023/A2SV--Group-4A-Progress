"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        depth = 0
        for ch in root.children:
            depth = max(depth, self.maxDepth(ch))
            
        return depth + 1
