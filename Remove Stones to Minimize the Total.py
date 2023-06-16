class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [- pile for pile in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            ope = heapq.heappop(piles)
            ope = ope // 2
            heapq.heappush(piles, ope)
        
        return - sum(piles)
