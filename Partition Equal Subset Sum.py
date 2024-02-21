class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dp(i, total):
            if total == target and i < len(nums):
                return True
            
            elif total > target or i >= len(nums):
                return False          

            curr_state = (i, total)

            if curr_state not in memo:
                memo[curr_state] = dp(i+1, total + nums[i]) or dp(i+1, total)

            return memo[curr_state]
        
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        
        memo = {}
        total = 0
        return dp(0, total)        
        
