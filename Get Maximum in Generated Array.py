class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [0] * (n+1)
        if n == 0:
            return 0
        dp[1] = 1
        
        for i in range(1,n+1):
            if 2*i <= n:
                
                dp[2*i] = dp[i]
            if 2*i + 1 <= n:
                dp[2 * i + 1] = dp[i] + dp[i + 1]
        return max(dp)
