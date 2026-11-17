class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if s[:]==s[::-1] else False