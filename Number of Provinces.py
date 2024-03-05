class UnionFind:
    def __init__(self, n):
        self.par_city = {}
        self.height = {}

        for i in range(n):
            self.par_city[i] = i
            self.height[i] = 1
            

    def find(self, city):
        if city == self.par_city[city]:
            return city
        return self.find(self.par_city[city])
        

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY: 
            if self.height[rootX] > self.height[rootY]:
                self.par_city[rootY] = rootX
                self.height[rootX] += self.height[rootY]

            else:
                self.par_city[rootX] = rootY
                self.height[rootY] += self.height[rootX]
    

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        solve = UnionFind(n)
        count = n
 
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and solve.find(i) != solve.find(j):
                    solve.union(i, j)
                    count -= 1

        return count


        
