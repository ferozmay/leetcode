"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        
        i = len(a) - 1
        j = len(b) - 1
        
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            total_sum = carry
            
            if i >= 0:
                total_sum += int(a[i])
                i -= 1  # Move the pointer to the left
            
            if j >= 0:
                total_sum += int(b[j])
                j -= 1  # Move the pointer to the left
            
            digit = total_sum % 2
            result.append(str(digit))
            
            carry = total_sum // 2
            
        return "".join(reversed(result))