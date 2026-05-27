class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                totalSum = a + nums[l] + nums[r]
                if totalSum < 0:
                    l += 1
                elif totalSum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return res