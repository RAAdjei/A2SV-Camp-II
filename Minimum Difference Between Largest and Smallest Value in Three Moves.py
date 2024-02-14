class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        nums.sort()
        l = 0
        n = len(nums)
        r = (n-3)-1
        mini = float('inf')

        while r < n:
            diff = nums[r] - nums[l]
            mini = min(mini, diff)
            l += 1
            r += 1

        return mini
