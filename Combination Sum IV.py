class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dp(total):
            if total == target:
                return 1
            if total > target:
                return 0

            if total not in memo:
                memo[total] = sum(dp(total + num) for num in nums)

            return memo[total]

        memo = {}
        return dp(0)
