class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.height = {}

        for i in range(n):
            self.root[i] = i
            self.height[i] = 1

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])  
        return self.root[node]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.height[rootX] > self.height[rootY]:
                self.root[rootY] = rootX
                self.height[rootX] += self.height[rootY] 
            elif self.height[rootX] < self.height[rootY]:  
                self.root[rootX] = rootY
                self.height[rootY] += self.height[rootX]  
            else:
                self.root[rootY] = rootX
                self.height[rootX] += 1



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        tree = UnionFind(n)

        for edge in edges:
            tree.union(edge[0], edge[1])

        return tree.find(destination) == tree.find(source)
