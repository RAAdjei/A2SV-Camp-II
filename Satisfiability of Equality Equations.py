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
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        uf = UnionFind(n)

        for string in equations:
            if string[1] == "=":     
                uf.union(string[0], string[-1])

        for string in equations:
            if uf.find(string[0]) == uf.find(string[-1]) and string[1] == "!":
                return False
        
        return True
