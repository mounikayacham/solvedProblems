class Solution:
	def minCoins(self, coins, sum):
		# code here
		dp=[float('inf')]*(sum+1)
		dp[0]=0
		for coin in coins:
		    for i in range(coin,sum+1):
		        dp[i]=min(dp[i],dp[i-coin]+1)
		#return dp[sum] if dp[sum] != float('inf') else -1
		return dp[sum] if dp[sum] != float('inf') else -1