# a very simple Algorithm for Solving the Connected Components But not the Best Solution for the large dataset


class Quick_Find:
    def __init__(self, N: int):
        self.arr = [i for i in range(N)]

    def connected(self, p, q):
        return self.arr[p] == self.arr[q]

    def union(self, p, q):
        pid = self.arr[p]
        qid = self.arr[q]
        for i in range(len(self.arr)):
            if self.arr[i] == pid:
                self.arr[i] = qid


uf = Quick_Find(10)
uf.union(1, 2)
uf.union(3, 4)
uf.union(1, 4)
uf.union(5, 6)
uf.union(5, 9)
uf.union(0, 5)
uf.union(7, 8)
uf.union(7, 0)
print(uf.arr)  # [9, 4, 4, 4, 4, 9, 9, 9, 9, 9] output
