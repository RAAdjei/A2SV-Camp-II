class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_dict = defaultdict(int)
        prefix_sum = 0
        sum_dict = {0:1}
        count = 0

        for i in range(len(nums)):
            num = nums[i]
            prefix_sum += num
            mod = prefix_sum % k

            if mod in sum_dict:
                count += sum_dict[mod]

            sum_dict[mod] = sum_dict.get(mod, 0) + 1

        return count
