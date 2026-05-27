class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        uniqueChars = set()
        length = 1
        while r < len(s):
            if s[r] in uniqueChars:
                l = r
                uniqueChars = set()
            else:
                uniqueChars.add(s[r])
                r += 1
            length = max(length, len(uniqueChars))

        return length
