class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        changed.sort()
        res = []
        i = 0
        j = 1
        n = len(changed)
        while n > 0 and j < n:
            if changed[i] * 2 == changed[j]:
                res.append(changed[i])
                n -= 2
                j = 1
                changed.pop(i)
                changed.pop(j)
                

            elif changed[i] * 2 > changed[j]:
                j += 1
            else:
                return []
        
        return res
        
