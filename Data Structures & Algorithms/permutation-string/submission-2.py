class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1freq = [0]*26
        s2freq = [0]*26

        for s in s1:
            s1freq[ord(s)-ord('a')] += 1
        
        win_size = len(s1)
        l, r = 0, 0
        while r < len(s2):
            s2freq[ord(s2[r])-ord('a')] += 1
            if r-l+1 == win_size:
                if s2freq == s1freq:
                    return True
                s2freq[ord(s2[l])-ord('a')] -= 1
                l += 1
            r +=1
        
        return False
        """
        if len(s1) > len(s2):
            return False

        s1freq = [0]*26
        s2freq = [0]*26

        for i in range(len(s1)):
            s1freq[ord(s1[i])-ord('a')] += 1
            s2freq[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1freq[i] == s2freq[i]:
                matches += 1

        print(matches) # we need to try to get this matches to 26

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r])-ord('a')
            s2freq[index] += 1
            if s1freq[index] == s2freq[index]:
                matches += 1
# you only want to decrement matches at a very specific moment: 
# when the count moves from being "equal" to "not equal."
            elif s1freq[index]+1 == s2freq[index]: 
                matches -= 1

            index = ord(s2[l])-ord('a')
            s2freq[index] -= 1
            if s1freq[index] == s2freq[index]:
                matches += 1
            elif s1freq[index]-1 == s2freq[index]:
                matches -= 1

            l += 1
        
        if matches == 26:
            return True
        else:
            return False
            













