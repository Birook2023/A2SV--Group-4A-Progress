# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])
        
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                queue.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)

        queue = deque([target.val])
        visited = set([target.val])

        while k and queue:
            k -= 1
            for _ in range(len(queue)):
                cur = queue.popleft()

                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        
        return list(queue)
