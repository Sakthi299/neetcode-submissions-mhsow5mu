class Solution:

    def encode(self, strs: List[str]) -> str:
        outputStr = ""
        for word in strs:
            outputStr += str(len(word))
            outputStr += '#'
            outputStr += word
        print(outputStr)
        return outputStr
    def decode(self, s: str) -> List[str]:
        res = [] 
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            lengthStr = int(s[i:j])
            res.append(s[j+1 : j+1+lengthStr])
            i = j+1+lengthStr
           
        return res
