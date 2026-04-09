import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)

            if len(minheap) > k:
                heapq.heappop(minheap)

        #print(minheap[0])
        return minheap[0]