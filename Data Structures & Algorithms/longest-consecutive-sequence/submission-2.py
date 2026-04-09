import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: 
            return 0
        if n == 1:
            return 1
        heapq.heapify(nums)

        seqMax = 1
        consSeq = 1
        val = heapq.heappop(nums)
        while len(nums) > 0:
            nextVal = heapq.heappop(nums)
            if nextVal == val:
                continue
            if nextVal == (val+1):
                consSeq +=1
                val = nextVal
            else:
                val = nextVal
                consSeq = 1
            
            seqMax = max(consSeq, seqMax)
        
        return seqMax


