class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)

        intervals.sort(key= lambda x:x[1])

        #print(intervals)

        count_non_overlapping_intervals = 1
        prev_end = intervals[0][1]

        for i in range(1, n, 1):
            if intervals[i][0] >= prev_end:
                count_non_overlapping_intervals += 1
                prev_end = intervals[i][1]
        
        #print(count_non_overlapping_intervals)

        return (n-count_non_overlapping_intervals)