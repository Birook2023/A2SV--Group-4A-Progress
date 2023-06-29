class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*len(quiet)
        
        
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        queue = deque()
        res=[i for i in range(len(quiet))]
        
        print(graph)
        print(indegree)

        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            
            for dest in graph[node]:
                if quiet[res[node]] < quiet[dest]:
                    res[dest] = res[node]
                    quiet[dest] = quiet[res[node]]
                indegree[dest] -= 1

                if indegree[dest] == 0:
                    queue.append(dest)
        
        return res

        
