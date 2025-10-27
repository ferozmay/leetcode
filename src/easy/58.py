"""
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()[::-1]

        ans = 0
        for i in range(len(s)):
            if s[i] == " ":
                return i
        
        return len(s)