from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        area = 0

        def bfs(point):
            nonlocal area
            currArea = 0
            visited.add(point)
            q = deque([point])
            while q:
                r, c = q.popleft()
                currArea += 1
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):
                            q.append((nr, nc))
                            visited.add((nr, nc))
            area = max(area, currArea)
                        


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs((i,j))
                    
        
        return area