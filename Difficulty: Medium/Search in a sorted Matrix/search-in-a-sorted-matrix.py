
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
    	n=len(mat)
    	m=len(mat[0])
    	i=0
    	j=m-1
    	while i<n and j>=0:
    	   if mat[i][j]==x:
    	       return True
    	   elif mat[i][j]>x:
    	       j-=1
    	   else:
    	       i+=1
    	return False
    	        
    	       
