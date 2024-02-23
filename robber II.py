class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return 0

        def robbery(end, start):
            memo = {}

            def dp(i):
                if i == start:
                    return nums[start]
                if i == start + 1:
                    return max(nums[start], nums[start + 1])
                if i not in memo:
                    memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
                return memo[i]

            return dp(end)

        return max(robbery(len(nums) - 2, 0), robbery(len(nums) - 1, 1))
