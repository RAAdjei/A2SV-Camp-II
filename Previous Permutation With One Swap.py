class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr) 
        if n < 2:
            return arr

        pos = -1
        for i in range(n-1, -1, -1):
            if arr[i-1] > arr[i]:
              pos = i-1
              break

        if pos == -1:
            return arr

        max_pos = pos+1
        for i in range(pos+1, n):
            if arr[i] >= arr[pos]:
                break
            if arr[i] > arr[max_pos]:
                max_pos = i

        arr[max_pos], arr[pos] = arr[pos], arr[max_pos]
        return arr

"""
Time - O(N)
space - O(1)
"""
