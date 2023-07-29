class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            
            if amount in memo:
                return memo[amount]
            count = float("inf")
            for coin  in coins:
                count = min(count, dp(amount-coin))
            result = count + 1
            memo[amount] = result
            return result
        final = dp(amount)
        if final == float("inf"):
            return -1
        return final
