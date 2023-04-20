class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        nums1 = nums[:n:2]
        rev_nums = nums[::-1]
        nums2 = rev_nums[0:n:2]
        ans = []
        
        for i in range(len(nums1)):
            ans.append(nums1[i] + nums2[i]) 
        
        return max(ans)
