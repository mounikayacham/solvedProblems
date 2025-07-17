#User function Template for python3
from itertools import permutations
class Solution:
    def findPermutation(self, s):
        # Code here
        return list(set(map(''.join, permutations(s))))

        
