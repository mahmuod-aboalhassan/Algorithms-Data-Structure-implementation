from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter = {}
        column_counter = {}
        n = len(grid)

        # Convert rows into tuple representations and count them
        for i in range(n):
            row = tuple(grid[i])  # use tuple to make it hashable for the dictionary
            row_counter[row] = row_counter.get(row, 0) + 1

        # Convert columns into tuple representations and count them
        for i in range(n):
            column = tuple(grid[j][i] for j in range(n))  # take ith element from each row to form a column
            column_counter[column] = column_counter.get(column, 0) + 1

        # Now count how many rows match with columns
        result = 0
        for row, count in row_counter.items():
            if row in column_counter:
                result += count * column_counter[row]

        return result
