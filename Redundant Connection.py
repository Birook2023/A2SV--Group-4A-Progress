class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        l = len(edges)
        parents = [x for x in range(l + 1)]

        def find(n):
            while parents[n] != n:
                n = parents[n]
            return n 
        
        def union(n1, n2):
            x = find(n1)
            y = find(n2)

            if x == y:
                return True
            parents[x] = parents[y]
            return False                

        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]
