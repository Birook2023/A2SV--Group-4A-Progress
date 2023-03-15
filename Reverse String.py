class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Using recursion method
        def Reverse(l, r):
            if l >= r:
                return 
            lis = s[l]
            s[l], s[r] = s[r] , lis
            
            return Reverse(l+1, r-1)
        return Reverse(0, len(s)-1)
