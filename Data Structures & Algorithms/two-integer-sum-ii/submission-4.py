class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        elements = {}
        for i in range(len(numbers)):
            if target - numbers[i] in elements:
                return [elements[target - numbers[i]]+1, i + 1]
            elements[numbers[i]] = i
        