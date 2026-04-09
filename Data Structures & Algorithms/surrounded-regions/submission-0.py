class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])

        unsurround = set()

        def dfs(r, c, visited):
            if (r<0 or c<0 or r>=rows or c>=cols or board[r][c] != 'O' or (r,c) in visited):
                return
            
            visited.add((r,c))
            board[r][c] = 'T'
            
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited)

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c, unsurround)
            if board[rows-1][c] == 'O':
                dfs(rows-1, c, unsurround)
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0, unsurround)
            if board[r][cols-1] == 'O':
                dfs(r, cols-1, unsurround)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        


