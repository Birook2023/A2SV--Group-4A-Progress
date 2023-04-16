class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i, j = 0, 1

        while j < len(nums) and i < j:
            if nums[i] == nums[j]:
                nums[i] = 2  * nums[i]
                nums[j] = 0
                i += 1
                j += 1
            else:
                i += 1
                j += 1
        
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        
        return nums
