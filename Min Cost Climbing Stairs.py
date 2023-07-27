class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        i,j = cost[0], cost[1]
        
        for a in range(2, n):
            k = cost[a] + min(i,j)
            i,j = j,k
        return min(i,j)
