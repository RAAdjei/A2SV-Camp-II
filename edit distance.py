class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dp(i,j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j

            if i == len(word1) and j == len(word2):
                return 0

            if (i,j) not in memo:
                if word1[i] == word2[j]:
                    memo[(i,j)] = dp(i+1, j+1)
                else:
                    memo[(i,j)] = 1 + min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1))
            
            return memo[(i,j)]


        memo = {}
        return dp(0,0)
