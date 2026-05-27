class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        setOfNums = set(nums)
        print(setOfNums)
        for i in setOfNums:
            temp = 1
            while i + 1 in setOfNums:
                temp += 1
                i += 1
            count = max(count, temp)
            
        return count