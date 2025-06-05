class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=s.split()
        r=k[-1]
        print(r)
        return len(r)
        
        