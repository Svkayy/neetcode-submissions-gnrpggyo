from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        count = 0

        def bfs(point):
            visited.add(point)
            q = deque([point])
            while q:
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == "1" and 
                        (nr, nc) not in visited):
                            q.append((nr, nc))
                            visited.add((nr, nc))
                        


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1
                    bfs((i,j))
                    
        
        return count
