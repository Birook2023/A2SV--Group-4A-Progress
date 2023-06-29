class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n


        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)
            indegree[a] += 1
            indegree[b] += 1
        queue = deque()
        
        for i in range(n):
            if indegree[i] <= 1:
                queue.append(i)
        res = []
        while queue:
            res = []

            for i in range(len(queue)):
                node = queue.popleft()
                res.append(node)

                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 1:
                        queue.append(neigh)
        return res
