class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0

        freq = defaultdict(int)
        while r < len(s):
            freq[s[r]] += 1

            # {Window Length} - {Count of Most Frequent Character} <= K
            while (r-l+1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1 

            res = max(res, r-l+1)
            r += 1
        
        return res
