class Solution:
    def minSteps(self, n: int) -> int:
        As, opr, cpy = 1, 0, 0
        
        while As < n:
            if n % As == 0:
                cpy = As
                opr += 1
            opr += 1
            As += cpy
        
        return opr
