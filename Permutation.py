class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = list(permutations([i+1 for i in range(n)]))
        return "".join(map(str, res[k-1]))
