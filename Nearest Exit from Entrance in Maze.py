class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        row, col = len(maze), len(maze[0])
        queue = deque()
        direc = ((0,1),(0,-1),(1,0),(-1,0))
        queue.append([entrance[0], entrance[1], -1])
        
        while queue:
            r, c, dist = queue.popleft()
            if not (0 <= r < row and 0 <= c < col):
                if dist > 0:
                    return dist
                continue
                
            if maze[r][c] == "+":
                continue
            maze[r][c] = "+"
            
            for i, j in direc:
                queue.append([r + i, c + j, dist + 1])
        return -1
