# A simple data structure for solving connected components using Quick Find.
# This is not the most efficient data structure  for large datasets as the union operation takes O(N) time.

class Quick_Find:
    # Constructor to initialize the array where each element is its own component initially
    def __init__(self, N: int):
        # Initialize an array of size N where each element represents its own component (id[i] = i)
        self.arr = [i for i in range(N)]

    # Method to check if two elements p and q are connected (i.e., belong to the same component)
    def connected(self, p, q):
        # If p and q have the same component id in the array, they are connected
        return self.arr[p] == self.arr[q]

    # Method to merge the components of p and q (connect them)
    def union(self, p, q):
        # Get the component id of p and q
        pid = self.arr[p]
        qid = self.arr[q]

        # Iterate through the array and change all entries with the component id of p to q's component id
        for i in range(len(self.arr)):
            if self.arr[i] == pid:
                # Merge component p into component q by assigning qid to all elements with pid
                self.arr[i] = qid

# Instantiate Quick_Find with 10 elements (0 through 9)
qf = Quick_Find(10)

# Perform union operations to connect elements
qf.union(1, 2)  # Connect component containing 1 with component containing 2
qf.union(3, 4)  # Connect component containing 3 with component containing 4
qf.union(1, 4)  # Connect component containing 1 (and thus 2) with component containing 4 (and thus 3)
qf.union(5, 6)  # Connect component containing 5 with component containing 6
qf.union(5, 9)  # Connect component containing 5 (and thus 6) with component containing 9
qf.union(0, 5)  # Connect component containing 0 with component containing 5 (and thus 6, 9)
qf.union(7, 8)  # Connect component containing 7 with component containing 8
qf.union(7, 0)  # Connect component containing 7 (and thus 8) with component containing 0 (and thus 5, 6, 9)

# Output the current state of the array, which represents the connected components
print(qf.arr)  # Expected output: [9, 4, 4, 4, 4, 9, 9, 9, 9, 9]

# Explanation:
# Elements that are in the same component will have the same value in the array.
# For example, element 0, 5, 6, 7, 8, and 9 are all in the same component, so they have the value 9.
# Similarly, elements 1, 2, 3, and 4 are all in the same component, so they have the value 4.
