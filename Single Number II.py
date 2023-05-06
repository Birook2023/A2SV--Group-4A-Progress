class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num >> i & 1:
                    count += 1
            if i == 31 and count % 3 != 0:
                res -= 1 << 31
            if count % 3:
                res |= 1 << i
        
        return res
