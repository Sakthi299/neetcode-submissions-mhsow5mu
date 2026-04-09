import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        freq = [0]*26

        for char in tasks:
            freq[ord(char)-ord('A')] +=1
        """
        freq = defaultdict(int)
        for task in tasks:
            freq[task] +=1
        
        maxheap = [-x for x in freq.values()]
        heapq.heapify(maxheap)

        time = 0
        dq = deque() #double ended queue

        while maxheap or dq:
            time +=1

            if maxheap:
                cnt=1+heapq.heappop(maxheap)
                if cnt:
                    dq.append([cnt, time+n])
                
            if dq and dq[0][1] == time:
                val = dq.popleft()[0]
                heapq.heappush(maxheap, val)
     

        return time
