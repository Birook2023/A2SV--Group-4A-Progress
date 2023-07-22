class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        Min = float('inf')
        Mid = float('inf')
        
        for num in nums:
            if num <= Min:
                Min = num
            elif num <= Mid:
                Mid = num
            else:
                return True
                
        return False
