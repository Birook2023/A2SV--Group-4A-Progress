class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        if c == 0 or c == 1:
            return True
        
        arr = []
        d = (c ** (1/2)) // 1
        
        for i in range(int(d)):
            arr.append(i)
        
        l, r = 0, d
        
        while l <= r:
            if (l * l) +( r * r) > c:
                r -= 1
            elif (l * l) +( r * r) < c:
                l += 1
            else:
                return True
        
        return False
        
