class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        f = float('inf')
        s = float('inf')
        for i in nums:
            if i <= f:
                f = i
            elif i <= s:
                s = i
            else:
                return True

        return False
