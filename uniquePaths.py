class Solution:
    def uniquePaths(self, m: int, n: int) -> int:        

        def dp(row, col):
            if (row, col) == target and row < m and col < n:
                return 1
            elif row == m or col == n:
                return 0

            curr_state = (row, col)

            if curr_state not in memo:
                memo[curr_state] = dp(row+1, col) + dp(row, col+1)

            return memo[curr_state]

        target = (m-1, n-1)
        memo = {}
        return dp(0, 0)
            


        
