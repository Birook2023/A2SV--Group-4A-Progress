class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^ 0 = 0
        # x^ -3 = (1/x) ^ 3  if x is negative when we call x --> 1/x and  n --> -1 * n
        # x^ 4 = x^2 * x^2  if x is even then call the function x --> x and n --> n/2 
        # x^ 3 = x^2 , x^1, x^ 0 if x is odd x --> x and b --> n-1 
        if n == 0: # base case
            return 1
        
        elif n < 0: # if negative
            return self.myPow(1/x, -n)
        
        elif n % 2 == 0: # if even
            var = self.myPow(x, n/2)
            return var * var
        
        else: # if odd
            return x * self.myPow(x, n-1)
        
