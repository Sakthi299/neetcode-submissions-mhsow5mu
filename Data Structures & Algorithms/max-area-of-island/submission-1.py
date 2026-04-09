class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r,c): # RECURSIVE FUNCTION
            #base case to fail
            if (r < 0 or r >= rows 
            or c < 0 or c >= cols or grid[r][c] == 0 or (r,c) in visited):
                return 0

            visited.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = dfs(r,c)
                    max_area = max(area, max_area)
        return max_area
        """
        # ITERATIVE DFS
        rows, cols = len(grid), len(grid[0])
        maxarea = 0
        islands = 0
        visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(row, col):
            stack = []
            area = 0
            visited.add((row,col))
            stack.append((row,col))
            while stack:
                r,c = stack.pop()
                area += 1
                for dr,dc in directions:
                    row, col = r+dr, c+dc
                    if (0 <= row < rows and 0 <= col < cols and
                    grid[row][col] == 1 and (row,col) not in visited):
                        visited.add((row,col))
                        stack.append((row,col))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area =  dfs(r,c)
                    islands += 1
                    maxarea = max(maxarea, area)
        #print("islands:", islands)
        #print("maxarea:", maxarea)
        return maxarea
        """
