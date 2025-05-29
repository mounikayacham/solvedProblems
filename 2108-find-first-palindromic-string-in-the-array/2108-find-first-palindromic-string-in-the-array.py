class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        p=[]
        def pallindrome(words):
            j=0
            k=len(words)-1
            while j<k:
                if words[j]!=words[k]:
                    return False
                j+=1
                k-=1
            return True
        for w in words:
            if pallindrome(w):
                return w
        return ""
           
            
            
        