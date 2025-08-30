class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i, numi in enumerate(nums):
       # numi + numj = target    rverse the equation
            if target - numi  in hashmap:
                return [hashmap[target - numi ],i]

            hashmap[numi] = i
