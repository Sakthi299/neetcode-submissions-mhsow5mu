from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        l = r = 0
        q = deque()

        while r < len(nums):
            #print("indexes", str(l), str(r))
            #print(q)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()
            
            if (r - l + 1) >= k:  # must have atleast k elements
                #print("deque: ", q)
                output.append(nums[q[0]])
                #print("output: ", output)
                l += 1
            r += 1

        return output