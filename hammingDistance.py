class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        new = x ^ y
        while new:
            if new & 1:
                count += 1
            new >>= 1

        return count
