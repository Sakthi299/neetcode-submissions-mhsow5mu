class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROW, COL = len(matrix), len(matrix[0])

        l, r = 0, ROW-1

        while l <= r:
            mid = l + (r-l)//2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        
        if l > r:         
            # ROW pointers crossed each other 
            # but target not present in ROW range 
            return False 
        
        row = (l + r) //2  # l + (r-l)//2 same as MID 
        l, r = 0, COL-1
        while l <= r:
            mid = l + (r-l)//2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False

