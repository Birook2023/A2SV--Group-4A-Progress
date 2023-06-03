# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque([root])
        visited = set()
        ans = []

        while queue:
            size = len(queue)
            level_sum = 0

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val
                visited.add(node)

                if node.left and node.left not in visited:
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    queue.append(node.right)

            ans.append(level_sum/size)

        return ans
