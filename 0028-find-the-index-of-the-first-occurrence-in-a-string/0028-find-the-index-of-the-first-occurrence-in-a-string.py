class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=len(haystack)
        n=len(needle)
        if n==h:
            if haystack==needle:
                return 0
        for i in  range(h-n):
            if haystack[i:i+n]==needle:
                return i
        return -1
