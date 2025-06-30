class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=s.split()
        r=k[-1]
        return len(r)