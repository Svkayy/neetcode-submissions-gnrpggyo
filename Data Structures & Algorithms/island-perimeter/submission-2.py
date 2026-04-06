from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        
        visited = set()

        def bfs(point):
            nonlocal perimeter
            visited.add(point)
            q = deque([point])
            while q:
                r, c = q.popleft()
                if grid[r][c] == 1:
                    perimeter += 4
                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            perimeter -= 1
                            if (nr, nc) not in visited:
                                visited.add((nr, nc))
                                q.append((nr, nc))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs((r,c))
                    return perimeter
        
        return perimeter

