import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        #print(maxheap)
        while len(maxheap) > 1:
            x = -1*heapq.heappop(maxheap)
            y = -1*heapq.heappop(maxheap)
            if x == y: 
                continue
            elif x != y:
                #print(-abs(x-y))
                heapq.heappush(maxheap,-abs(x-y))

        if maxheap:
            return -maxheap[0]
        else: 
            return 0


