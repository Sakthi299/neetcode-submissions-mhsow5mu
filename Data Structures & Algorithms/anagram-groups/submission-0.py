class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            charcount = [0] * 26           
            for char in s:
                charcount[ord(char.lower())-ord('a')] +=1
            hashmap[tuple(charcount)].append(s)

        values = []
        #print(hashmap.items())
        for key, value in hashmap.items():
            values.append(value)
                
        return values