from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        rot = []
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rot.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                else: 
                    continue
        
        q = deque(rot)
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < rows and 
                       0 <= nc < cols and
                       grid[nr][nc] == 1):
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                            fresh -= 1
            time += 1
        
        if fresh > 0:
            return -1

        return time