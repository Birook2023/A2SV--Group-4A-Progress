class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        ind = 0
        r = len(nums) - 1 
        while c <= r:
            if nums[ind] == 0:
                nums[ind], nums[l] = nums[l], nums[ind]
                ind += 1
                l += 1
            elif nums[ind] == 2:
                nums[ind], nums[r] = nums[r], nums[ind]
                r -= 1
            else:
                ind += 1
