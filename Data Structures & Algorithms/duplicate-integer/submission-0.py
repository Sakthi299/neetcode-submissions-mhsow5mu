class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()
        for num in nums:
            if num in uniqueSet:
                return True
            uniqueSet.add(num)
            #print(num)
        return False
        