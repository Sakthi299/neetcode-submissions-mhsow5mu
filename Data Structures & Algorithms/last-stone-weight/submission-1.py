import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -stone)
        
        #print(maxheap)
        while len(maxheap) > 1:
            val1 = -heapq.heappop(maxheap)
            val2 = -heapq.heappop(maxheap)

            if val1-val2 > 0:
                heapq.heappush(maxheap, -1 * (val1-val2))
            
        #print(maxheap)

        return -maxheap[0] if maxheap else 0
            
       


