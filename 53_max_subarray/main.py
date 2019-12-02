class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        dp = [None] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[1] + dp[0])
        largest = max(dp[1], dp[0])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            if dp[i] > largest:
                largest = dp[i]
            
        return largest

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution().maxSubArray(nums)
print(sol)