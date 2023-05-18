class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        
    def vertex(self, u):
        print(*self.adj[u])
        
n = int(input())
k = int(input())
g = Graph(n)
for i in range(k):
    op = list(map(int, input().split()))
    if op[0] == 1:
        g.add_edge(op[1] - 1, op[2] - 1)
    else:
        g.vertex(op[1] - 1)
