#Function to locate the occurrence of the string x in the string s.
class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        pos=-1
        for i in range(len(txt)-len(pat)+1):
            if txt[i:i+len(pat)]==pat:
                pos=i
                break
        return pos