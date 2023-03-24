class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)

        while l <= r:
            mid = l + (r - l) // 2
            count = 0
            for num in nums:
                count += ceil(num / mid)
            if count > threshold:
                l = mid + 1
            elif count <= threshold:
                r = mid - 1
                ans = r
        return ans + 1
