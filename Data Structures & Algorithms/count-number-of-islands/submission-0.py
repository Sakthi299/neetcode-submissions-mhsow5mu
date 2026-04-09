from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        """ 
        BFS - Iterative Approach
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            q = deque()
            visited.add((row,col))
            q.append((row,col))

            while q:
                r, c = q.popleft()

                directions = [[0,1], [0,-1],[1,0],[-1,0]]

                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (0 <= row < rows and 0 <= col < cols 
                    and grid[row][col] == "1" and (row,col) not in visited):
                        visited.add((row,col))
                        q.append((row,col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
                
        return islands
        """
        """
        DFS 
        Iterative Approach
        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(row, col):
            stack = []
            visited.add((row,col))
            stack.append((row,col))
            while stack:
                r, c = stack.pop()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (0 <= row < rows and 0 <= col < cols and
                    grid[row][col] == "1" and (row,col) not in visited):
                        stack.append((row,col))
                        visited.add((row,col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        return islands

