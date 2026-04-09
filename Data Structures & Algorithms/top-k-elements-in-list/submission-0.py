class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1

        sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item:item[1], reverse=True)) 
    
        count = 1
        output = []
        
        for key, value in sorted_hashmap.items():
            if count <=k: 
                output.append(key)
                count +=1
        
        return output