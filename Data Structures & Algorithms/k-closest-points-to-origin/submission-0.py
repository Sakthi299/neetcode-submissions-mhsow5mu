class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        minheap = []
        for point in points:
            dis = (point[0]*point[0]) + (point[1]*point[1])
            heapq.heappush(minheap, [dis,[point[0], point[1]]])
        
        while k > 0:
            result.append(heapq.heappop(minheap)[1])
            k -=1
        
        return result
        
