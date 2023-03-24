class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l, r = 1, len(arr) - 2

        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid - 1] > arr[mid] > arr[mid + 1]:
                r = mid - 1
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                return mid
        
