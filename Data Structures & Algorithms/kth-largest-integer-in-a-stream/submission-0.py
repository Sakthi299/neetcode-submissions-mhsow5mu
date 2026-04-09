import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        minheap = []

        for num in self.nums:
            heapq.heappush(minheap, num)
            if len(minheap) > self.k:
                heapq.heappop(minheap)
        
        self.nums = minheap

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]
        
