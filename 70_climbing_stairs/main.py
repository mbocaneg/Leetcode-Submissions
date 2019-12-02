# 1 -> [1]
# 2 -> {1 + 1}, 2  [2]
# 3 -> {1 + 1 + 1}, {1 + 2, 2 + 1}  [3]
# 4 -> {1 + 1 + 1 + 1}, {2 + 1 + 1}, {1 + 2 + 1}, {1 + 1 + 2}, {2 + 2}  [5]

class Solution:
    def climbStairs(self, n):
        if n < 2:
            return 1
        
        dp = [None] * n

        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]

n = 5
sol = Solution().climbStairs(n)
print(sol)
