
class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.height = {}

        for i in range(1, n+1):
            self.root[i] = i
            self.height[i] = 1

    def find(self, node):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, x , y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False

        if self.height[rootX] > self.height[rootY]:
            self.root[rootY] = rootX
        elif self.height[rootX] < self.height[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.height[rootX] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        tree = UnionFind(n)
        output = []

        for edge in edges:
            if not tree.union(edge[0], edge[1]):
                output = edge

        return output
