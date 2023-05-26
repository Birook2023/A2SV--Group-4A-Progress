class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        minute = 0
        fresh = 0
        directions = [[0,1], [1,0], [0,-1], [-1,0]] 
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i,j])
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == n or col < 0 or col == m or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            minute += 1
        
        
        if fresh == 0: 
            return minute 
        else :
            return -1
