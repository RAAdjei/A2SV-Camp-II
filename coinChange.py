def dp(total):
            if total == amount:
                return 0

            
            mini = float("inf")
            if total not in memo:
                for coin in coins:
                    if total+coin <= amount:
                        mini = min(mini, 1+dp(total+coin))
                memo[total] = mini

            
            return memo[total]

        memo = {}
        if dp(0) != float("inf"):
            return dp(0)
        else: 
            return -1 
