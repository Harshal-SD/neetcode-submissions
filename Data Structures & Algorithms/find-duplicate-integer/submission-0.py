class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        uniqueNum = set()

        for num in nums:
            if num in uniqueNum:
                return num
            uniqueNum.add(num)