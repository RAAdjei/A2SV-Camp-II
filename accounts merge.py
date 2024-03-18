class UnionFind:
    def __init__(self, accounts):
        self.root = {}
        self.firstName = {}

        for acct in accounts:
            for j in range(1, len(acct)):
                self.root[acct[j]] =  acct[j]
                self.firstName[acct[j]] = acct[0]


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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(accounts)
        output = []
        emails = defaultdict(list)

        for acct in accounts:
            for i in range(2, len(acct)):
                uf.union(acct[i], acct[i-1])

        for email in uf.root:
            emails[uf.find(email)].append(email)

        for val in emails:
            output.append([uf.firstName[val]] + sorted(emails[val]))

        return output
