class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        maxarea = float('-inf')

        while l<r:
            y= min(heights[l], heights[r])
            x= r-l
            if y*x > maxarea:
                maxarea = y*x
            if heights[l] < heights[r]:
                l +=1
            elif heights[l] >= heights[r]:
                r -=1
            
        return maxarea
