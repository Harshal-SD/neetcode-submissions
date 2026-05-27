class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            count = 1
            while num + 1 in nums:
                num += 1
                count += 1
            if count > res:
                res = count
        return res