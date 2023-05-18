class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        test = image[sr][sc]
        dirc = [0,1],[0,-1],[1,0],[-1,0]
        visited = set()
        
        def solve(r, c):
            return (0 <= r < len(image)) and (0 <= c < len(image[0]))
        
        def dfs(node):
            visited.add((node[0],node[1]))
            
            for di,dj in dirc:
                nr = di + node[0]
                nc = dj + node[1]
                if  (nr,nc) not in visited:
                    if solve(nr,nc) and image[nr][nc] == test:
                        image[nr][nc] = color
                        dfs([nr,nc])
        dfs([sr,sc])
        image[sr][sc] = color
        
        return image
