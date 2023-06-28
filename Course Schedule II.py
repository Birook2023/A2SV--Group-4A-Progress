class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        queue = deque()
        print(indegree)
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        order = []
        print(indegree)
        print(queue)
        while queue:
            node = queue.popleft()
            order.append(node)

            for neign in graph[node]:
                indegree[neign] -= 1

                if indegree[neign] == 0:
                    queue.append(neign)
        
        return order if len(order) == numCourses else []
        graph = defaultdict(list)
        indegree = [0] * numcources
        
        
