class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                if hashmap[diff] > i :
                    return [i, hashmap[diff]]
                else:
                    return [hashmap[diff], i]
            hashmap[nums[i]] = i
            