"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start, end = [], []

        for inv in intervals:
            start.append(inv.start)
            end.append(inv.end)
        
        start.sort()
        end.sort()
        count = max_count = 0
        i = j = 0

        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            max_count = max(count, max_count)

        return max_count




        

        