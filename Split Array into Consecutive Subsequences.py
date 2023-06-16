class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        arr = []

        for num in nums:
            while arr and arr[0][0] + 1 < num:
                a = heapq.heappop(arr)
                if a[1] < 3:
                    return False
            if not arr or arr[0][0] == num:
                heapq.heappush(arr, (num, 1))
            else:
                b = heapq.heappop(arr)
                heapq.heappush(arr, (num, b[1] + 1))
        
        for num, leng in arr:
            if leng < 3:
                return False
        
        return True
