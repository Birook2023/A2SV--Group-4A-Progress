class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def dp(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            elif n == 3:
                return 2
            if n in memo:
                return memo[n]
            result = dp(n-3) + dp(n- 2) + dp(n-1)
            memo[n] = result
            return result
        result = dp(n)
        return result
