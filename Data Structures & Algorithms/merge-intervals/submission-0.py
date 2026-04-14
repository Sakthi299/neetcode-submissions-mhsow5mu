class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        result = [] # result set

        intervals.sort(key= lambda x:x[0]) # sort intervals

        result.append(intervals[0]) # 1st item

        for i in range(1, len(intervals)):
            last = result[-1]              # get last end time

            if intervals[i][0] <= last[1]: # if next start <= end time, extend the result set 
                last[1] = max(last[1], intervals[i][1])
            else:                          # if next start > end time, add to the result set
                result.append(intervals[i])

        return result
