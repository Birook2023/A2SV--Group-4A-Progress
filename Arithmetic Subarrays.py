class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            s = sorted(nums[l[i] : r[i] + 1])
            arth = True
            for j in range(len(s) - 1):
                if s[j + 1] - s[j] != s[1] - s[0]:
                    arth = False
                    break
            res.append(arth)
        return res
