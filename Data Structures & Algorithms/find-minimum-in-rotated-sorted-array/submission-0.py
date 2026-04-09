class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 4 5 1 2 
        n = len(nums)

        l, r = 0, n-1

        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]