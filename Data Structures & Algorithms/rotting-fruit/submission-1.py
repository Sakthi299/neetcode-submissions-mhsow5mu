from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        minute = 0
        q = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c,minute))
        
        while q:
            r,c, minute = q.popleft()
            
            print("minute: ", minute)
            for dr,dc in directions:
                row, col = r+dr, c+dc
                if ( 0<=row<rows and 0<=col<cols and 
                grid[row][col] == 1 and (row,col) not in visited):
                    grid[row][col] = 2
                    visited.add((row,col))
                    q.append((row,col,minute+1))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minute




        