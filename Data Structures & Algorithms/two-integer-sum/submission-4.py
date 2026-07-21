class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_num = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dict_num:
                return [dict_num[difference], i]
            dict_num[nums[i]] = i