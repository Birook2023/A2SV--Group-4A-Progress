class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        
        for nums in matrix:
            for num in nums:
                arr.append(num)
        
        heapq.heapify(arr)
        for _ in range(k):
            res = heapq.heappop(arr)
        
        return res
