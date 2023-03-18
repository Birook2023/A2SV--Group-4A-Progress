class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x

        while l <= h:
            mid = l + (h - l)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                h = mid - 1
            else:
                l += 1
                var = mid
        
        return var

        
