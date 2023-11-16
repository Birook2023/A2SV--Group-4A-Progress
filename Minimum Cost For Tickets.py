class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        m = days[-1]
        res = [0] * (m + 1)
        travel = [False] * (m + 1)
        for d in days:
            travel[d] = True
        for i in range(1, m + 1):
            if travel[i]:
                res[i] = min(res[i - 1] + costs[0], res[max(0, i - 7)] + costs[1], res[max(0, i - 30)] + costs[2])
            else:
                res[i] = res[i - 1]
        return res[-1]
