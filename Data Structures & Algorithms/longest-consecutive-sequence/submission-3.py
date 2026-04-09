import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
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
        """
        n = len(nums)

        hashset = set(nums)

        maxSeq = 0
        for num in nums:
            if num-1 not in hashset:
                counter = 0
                while num+counter in hashset:
                    counter += 1
                maxSeq = max(maxSeq, counter)
        
        return maxSeq


