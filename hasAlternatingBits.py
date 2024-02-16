class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = n ^(n >> 1)
        return num.bit_length() == num.bit_count()
            
