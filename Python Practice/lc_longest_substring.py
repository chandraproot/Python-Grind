# Given a string s, find the length of the longest 
# substring
#  without repeating characters.
from typing import SupportsInt
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

s = "bbbbb"
obj = Solution()
result = obj.lengthOfLongestSubstring(s)
print(result)