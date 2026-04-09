from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-Source BFS
        (visited set is not needed, as we can change fresh to rotten orange value 
        to mark it as seen)
        """
        rows, cols = len(grid), len(grid[0])    
        q = deque()
        fresh, time = 0, 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                
        while q and fresh > 0:
            layers = len(q)
            for _ in range(layers):
                r,c = q.popleft()
                for dr,dc in directions:
                    row, col = r+dr, c+dc
                    if (0<=row<rows and 0<=col<cols and
                    grid[row][col]==1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1



        