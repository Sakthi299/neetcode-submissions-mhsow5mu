"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        minheap = []
        if not intervals:
            return True

        for item in intervals:
            heapq.heappush(minheap, (item.start, item.end))


        s, inite = heapq.heappop(minheap)
        while len(minheap) > 0:
            s, e = heapq.heappop(minheap)
            if s < inite:
                return False
            inite = e
        
        return True