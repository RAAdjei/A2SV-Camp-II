class UnionFind:
    def __init__(self, n):
        self.root = {}
        for i in range(26):
            self.root[chr(ord('a')+i)] = chr(ord('a')+i)


    def find(self, node):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]


    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if rootX > rootY:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
           

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        tree = UnionFind(n)
        output = []

        for i in range(n):
            tree.union(s1[i], s2[i])

        for i in baseStr:
            output.append(tree.find(i))

        return "".join(output)
