class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if pa < pb: 
                parent[pb] = pa
            else:
                parent[pa] = pb
        
        for a, b in zip(s1, s2):
            x = ord(a)-ord("a")
            y = ord(b)-ord("a")
            union(x, y)

        res = ""
        for ch in baseStr:
            res += chr(ord("a") + find(ord(ch)-ord("a")))
        return res
