class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_freq = [0]*26

        s1_len = len(s1)

        for char in s1:
            s1_freq[ord(char)-ord('a')] +=1
        
        l, r = 0, 0
        hashmap = [0]*26
        while r < len(s2):
            hashmap[ord(s2[r])-ord('a')] += 1

            if r-l+1 == s1_len:
                #print("hash:", hashmap)
                if hashmap != s1_freq:
                    hashmap[ord(s2[l])-ord('a')] -= 1
                    l += 1
                else:
                    return True
            
            r += 1

        return False