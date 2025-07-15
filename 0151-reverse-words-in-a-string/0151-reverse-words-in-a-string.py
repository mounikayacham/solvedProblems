class Solution:
    def reverseWords(self, s: str) -> str:
        k=s.split()
        p=k[::-1]
        return ' '.join(p)