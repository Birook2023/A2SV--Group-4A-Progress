class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []

        num= sorted(nums)

        for i in range(len(nums)):
            ans.append(num.index(nums[i]))

        return ans
