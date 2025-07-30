class Solution:
    def cntSubarrays(self, nums, k):
        # code here
        from collections import defaultdict

        count = 0
        curr_sum = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # Initialize with sum 0 having one occurrence
    
        for num in nums:
            curr_sum += num
            if (curr_sum - k) in prefix_sum:
                count += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] += 1
    
        return count
