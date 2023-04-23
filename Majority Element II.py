class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = Counter(nums)
        res = []
        
        for i, j in m.items():
            if j > n // 3:
                res.append(i)
        return res
