def dp(i):
            if i > len(nums)-1:
                return
        
            if i % 2 == 0 and i not in memo:
                val = i // 2
                nums[i] = nums[val]
                memo[i] = dp(i+1)

            elif i % 2 == 1 and i not in memo:
                val = i // 2
                nums[i] = nums[val] + nums[val + 1]
                memo[i] = dp(i+1)

            return memo[i]

        
        nums = [0] * (n+1)
        memo = {}
        if len(nums) >= 2:
            nums[1] = 1
            i = 2
        else:
            i = 0
        
        dp(i)
        return max(nums) 
