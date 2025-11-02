"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        a = x # Start with an initial guess
        
        # Iterate until a*a is no longer greater than x
        while a > x // a:
            print("Loop iteration")
            print(a)
            a = (a + x // a) // 2
            print(a)
            print()
        return a
    


sol = Solution()
print(sol.mySqrt(100))  # Expected output: 2