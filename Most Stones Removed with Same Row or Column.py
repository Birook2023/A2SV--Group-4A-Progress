class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parents = list(range(len(stones)))
        ranks = [1] * len(stones)
        rows, columns  = {},{}
        
        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
        
        def union(i, j):
            i, j = find(i), find(j)
            if i == j:
                return False
            elif ranks[i] > ranks[j]:
                parents[j] = i
                ranks[i] += ranks[j]
            else:
                parents[i] = j
                ranks[j] += ranks[i]
            return True
        
        res = 0
        for k, (row, col) in enumerate(stones):
            if row in rows and union(k, rows[row]):
                res += 1
            if col in columns and union(k, columns[col]):
                res += 1
            rows[row] = columns[col] = k
        
        return res
