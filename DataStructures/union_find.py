class Union_Find:
    def __init__(self,N: int) -> None:
        self.parent=list(range(N))
        self.rank=[1]*N
    def find(self,i):
        while i!= self.parent[i]:i=self.parent[i]
        return i 
    def connected(self,p,q):
        return self.parent[p]== self.parent[q]
    def union(self,p,q):
        i=self.find(p)
        j=self.find(q)
        self.parent[i]=j

uf = Union_Find(10)

# Perform union operations to connect elements
uf.union(1, 2)  # Connect component containing 1 with component containing 2
uf.union(3, 4)  # Connect component containing 3 with component containing 4
uf.union(1, 4)  # Connect component containing 1 (and thus 2) with component containing 4 (and thus 3)
uf.union(5, 6)  # Connect component containing 5 with component containing 6
uf.union(5, 9)  # Connect component containing 5 (and thus 6) with component containing 9
uf.union(0, 5)  # Connect component containing 0 with component containing 5 (and thus 6, 9)
uf.union(7, 8)  # Connect component containing 7 with component containing 8
uf.union(7, 0)  # Connect component containing 7 (and thus 8) with component containing 0 (and thus 5, 6, 9)

# Output the current state of the array, which represents the connected components
print(uf.parent)  # Expected output: [9, 2, 4, 4, 4, 6, 9, 8, 9, 9]
