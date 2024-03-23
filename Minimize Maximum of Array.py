class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = tot = nums[0]
        n = len(nums)

        for i in range(1, n):
            tot += nums[i]
            ans = max(ans, math.ceil(tot / (i+1)))

        return ans
        
