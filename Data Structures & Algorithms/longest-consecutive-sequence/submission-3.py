class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        setOfNums = set(nums)
        print(setOfNums)
        for num in setOfNums:
            if num - 1 not in setOfNums:
                temp = 1
                while num + temp in setOfNums:
                    temp += 1
                count = max(count, temp)
        return count