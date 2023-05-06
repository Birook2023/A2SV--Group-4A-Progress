class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        a = x ^ y
        
        while a:
            ans += 1
            a &= a - 1
        
        return ans
            
        
