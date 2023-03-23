l, r = 1, max(piles)
        
        while l < r:
            k = l + (r - l)//2
            reqhr = 0
            for pile in piles:
                reqhr += (pile + k - 1) // k

            if reqhr > h:
                l = k + 1
            else:
                r = k 
        
        return r
