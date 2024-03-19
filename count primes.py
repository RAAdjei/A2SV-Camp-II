class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        arr = [True for i in range(n)]
        arr[0] = arr[1] = False
   
        count = 0
        for i in range(2, n):
            if arr[i] == True:
                count += 1
                for j in range(i**2, n, i):
                    arr[j] = False

        return count

        
        
