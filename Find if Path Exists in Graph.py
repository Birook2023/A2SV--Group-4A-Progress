class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]

        def union(child, parent):
            ch = find(child)
            pa = find(parent)
            parents[ch] = parents[pa]

        def find(child):
            if parents[child] == child:
                return child
            return find(parents[child])

        for a, b in edges:
            union(a, b)
        return find(source) == find(destination)
