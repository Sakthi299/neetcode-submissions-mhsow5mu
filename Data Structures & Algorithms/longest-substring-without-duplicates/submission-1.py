class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()

        consSeq = 0
        i, j = 0, 0
        while j < len(s):
            while s[j] in hashset:
                hashset.remove(s[i])
                i += 1
            hashset.add(s[j])
            consSeq = max(consSeq, j-i+1)
            j += 1

        return consSeq