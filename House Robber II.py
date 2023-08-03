class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        if n == 3:
            return max(nums)
        a=[0]*(n-1)
        b=[0]*(n-1)

        a[0], a[1] = nums[0], max(nums[0:2])
        b[0], b[1] = nums[1], max(nums[1:3])
        
        for i in range(2, n-1):
            a[i]=max(a[i-2] + nums[i], a[i-1])
            b[i]=max(b[i-2] +nums[i+1], b[i-1])
        
        return max(a[-1], b[-1])
