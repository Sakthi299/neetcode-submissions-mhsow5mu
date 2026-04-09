class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # original array
        # 1, 2, 4, 6
        # 1, 2, 8, 48
        # 48 ,48 ,24 ,6

        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n

        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
        for i in range(1, n, 1):
            prefix[i] = prefix[i-1] * nums[i]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        print(prefix)
        print(suffix)

        result = [0]*n
        for i in range(n):
            left_edge = 1
            right_edge = 1

            if i<1:
                result[i] = left_edge * suffix[i+1]
            if i>n-2:
                result[i] = right_edge * prefix[i-1]
            if i > 0 and i < n-1:
                result[i] = prefix[i-1] * suffix[i+1]

        return result