class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + (r-l)//2

            totalHour = 0
            for p in piles:
                totalHour += (p+mid-1)//mid
            
            if totalHour <= h:
                res = mid
                r = mid - 1
            elif totalHour > h:
                l = mid + 1
        
        return res
                
            
        