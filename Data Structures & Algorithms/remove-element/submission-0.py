class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = len(nums)
        k = 0

        for i in range(n):
            if nums[i] != val:
                #nums[k] = nums[i] 
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        #print(nums)
        return k