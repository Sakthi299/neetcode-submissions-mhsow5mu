class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            freq = [0]*26
            for char in s:
                freq[ord(char)-ord('a')] += 1
            for char in t:
                freq[ord(char)-ord('a')] -= 1
            for i in freq:
                if i != 0:
                    return False
            return True
        else:
            return False
        """
        if len(s) == len(t):
            t = "".join(sorted(t, reverse=True))
            s = "".join(sorted(s))
            print(t)
            print(s)
            stack = []
            for char in s:
                stack.append(char)
            for i in range(len(t)):
                if stack and stack[-1] != t[i]:
                    return False
                stack.pop()
            
            if not stack:
                return True
            else: 
                return False
        else:
            return False
        """