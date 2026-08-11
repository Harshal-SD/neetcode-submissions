class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):

            if nums[i] == -1:
                return nums[i]

            nums[i] == -1
        