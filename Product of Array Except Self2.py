class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        suff = [1] * n
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        print(pre)
        print(suff)
        ans = []

        for i in range(n):
            ans.append(pre[i] * suff[i])
        return ans
