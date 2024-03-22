class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        n = len(nums)

        for i in range(2**n):
            sub = 0
            for j in range(n):
                if i & (1 << j):
                    sub |= nums[j]

            dict[sub] += 1

        x = max(dict.keys())
        return dict[x]
