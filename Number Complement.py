class Solution:
    def findComplement(self, num: int) -> int:
        bina = bin(num)[2:]
        res = ''.join(['0' if b == '1' else '1' for b in bina])
        
        return int(res, 2)
