class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            #print(diff)
            if diff in hashmap:
                if i < hashmap[diff]:
                    return [i, hashmap[diff]]
                else:
                    return [hashmap[diff], i]
            hashmap[nums[i]] = i
        
        #return []
