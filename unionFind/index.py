class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Recursively find the root
        return self.parent[x]

    def union(self, x, y):

        rootX = self.find(x)
        rootY = self.find(y)

        # Only unite if they have different roots
        if rootX != rootY:
            # Union by rank: attach smaller tree under the root of the larger tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                # If ranks are equal, make one root the parent of the other and increase its rank
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        # Check if two nodes are in the same set
        return self.find(x) == self.find(y)

uf = UnionFind(5)

# Union some sets 
uf.union(0,1)
uf.union(1,2)
uf.union(3,4)

print(uf.connected(0,2))
print(uf.connected(0, 3)) 
