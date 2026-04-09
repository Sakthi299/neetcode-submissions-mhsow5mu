from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        dist = 0 # initializing distance 
        while q:
            for _ in range(len(q)):  # level by level distance calculation
                row, col = q.popleft()
                grid[row][col] = dist
                for dr  , dc in directions:
                    r, c = row+dr, col+dc
                    if ( 0<=r<rows and 0<=c<cols and grid[r][c] != -1 and (r,c) not in visited ):
                        grid[r][c] = grid[row][col]+1
                        visited.add((r,c))
                        q.append((r,c))
            dist += 1  # incrementing distance at every level


        """
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in visited:
                    visited.add((r,c))
                    q.append((r,c))
                
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if ( 0<=r<rows and 0<=c<cols and 
                grid[r][c] != -1 and (r,c) not in visited ):
                    grid[r][c] = grid[row][col] + 1
                    visited.add((r,c))
                    q.append((r,c))
        """
        

