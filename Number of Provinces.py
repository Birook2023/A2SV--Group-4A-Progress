class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        1 0 0
        0 1 0
        0 0 1
        
        '''
        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] and j not in visited:
                    dfs(j)
        provs = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                provs += 1
                dfs(i)
        return provs
        
        
