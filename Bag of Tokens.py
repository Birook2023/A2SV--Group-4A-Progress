class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens)-1
        i, j = 0, 0
        
        while l <= r:
            if tokens[l] <= power:
                i += 1
                power -= tokens[l]
                l += 1
                j = max(j,i)
            elif power < tokens[l] and i > 0:
                i -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        
        return j
