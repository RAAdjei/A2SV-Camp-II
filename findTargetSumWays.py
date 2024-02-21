class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(i, curr_sum):
            if i > len(nums)-1:
                if curr_sum == target:
                    return 1
                else:
                    return 0

            curr_state = (i, curr_sum)

            if curr_state not in memo:
                pos = dp(i+1, nums[i]+curr_sum)
                neg = dp(i+1, -nums[i]+curr_sum)
                memo[curr_state] = pos + neg

            return memo[curr_state]
        
        memo = {}
        return dp(0, 0)
            
