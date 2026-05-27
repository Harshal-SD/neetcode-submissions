class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l = 0
        r = 0
        uniqueChars = set()
        length = 1
        while r < len(s):
            if s[r] in uniqueChars:
                l = r
                length = max(length, len(uniqueChars))
                uniqueChars = set()
            else:
                uniqueChars.add(s[r])
                r += 1

        return length
