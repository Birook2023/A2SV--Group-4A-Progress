class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            sums[i + 1] = sums[i] + nums[i]
        sums.pop(0)
        return sums
