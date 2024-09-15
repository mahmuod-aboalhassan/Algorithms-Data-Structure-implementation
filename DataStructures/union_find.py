class Union_Find:
    def __init__(self, N: int) -> None:
        self.parent = list(range(N))
        self.rank = [1] * N  # Rank represents the height of the tree.

    def find(self, i):
        # Path compression heuristic
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        
        if i == j:
            return  # Already in the same set
        
        # Union by rank: Attach smaller tree under the root of the larger tree.
        if self.rank[i] > self.rank[j]:
            self.parent[j] = i
        elif self.rank[i] < self.rank[j]:
            self.parent[i] = j
        else:
            self.parent[j] = i
            self.rank[i] += 1  # Increase rank when ranks are equal

# Testing the corrected implementation
uf = Union_Find(10)

# Perform union operations to connect elements
uf.union(1, 2)
uf.union(3, 4)
uf.union(1, 4)
uf.union(5, 6)
uf.union(5, 9)
uf.union(0, 5)
uf.union(7, 8)
uf.union(7, 0)

# Output the current state of the array, which represents the connected components
print(uf.parent)  # This will show the parent of each element
print(uf.rank)    # This shows the rank (tree height) of each component's root
