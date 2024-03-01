class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        pre_total = 0
        res = 0

        for sat in satisfaction:
            pre_total += sat
            if pre_total < 0:
                break
            else:
                res += pre_total

        return res
        
