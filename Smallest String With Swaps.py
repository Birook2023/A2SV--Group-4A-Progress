class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        def union(a,b):
            parent[find(a)] = find(b)
        for a,b in pairs:
            union(a,b)
        print(parent)
        g = defaultdict(list)
        g2 =  defaultdict(list)
        
        for i in range(len(s)):
            g[find(i)].append(i)
            g2[find(i)].append(s[i])

        ans = [""] * len(s)
        for k in g.keys():
            ix = sorted(g[k])
            ch = sorted(g2[k])
            for i,c in zip(ix, ch):
                ans[i] = c
        return "".join(ans)

        
