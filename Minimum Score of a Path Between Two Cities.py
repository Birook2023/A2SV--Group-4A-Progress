class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for road in roads:
            adj_list[road[0]].append((road[1], road[2]))
            adj_list[road[1]].append((road[0], road[2]))
        
        print(adj_list)
        min_val = float('inf')
        queue = deque()
        queue.append(1)
        visited = set()
        visited.add(1)
        
        while queue:
            node = queue.popleft()
            
            for val in adj_list[node]:
                x, y = val[0], val[1]
                min_val = min(min_val, y)
               
                if x not in visited:
                    queue.append(x)
                    visited.add(x)
        return min_val
