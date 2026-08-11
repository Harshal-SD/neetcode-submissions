class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0, 0
        maxlen = 0
        uniquechar = {}
        while r < len(s):
            if s[r] not in uniquechar:
                uniquechar[s[r]] = 1
            else:
                maxlen = max(maxlen, r - 1 - l + 1)
                while s[r] in uniquechar:
                    del uniquechar[s[l]]
                    l += 1
                uniquechar[s[r]] = 1
            r += 1
        return maxlen