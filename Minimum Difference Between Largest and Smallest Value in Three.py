class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums) - 4
        dif = float("inf")

        for i in range(len(nums)- n):
            dif = min(dif, nums[i+n] - nums[i])

        return dif
