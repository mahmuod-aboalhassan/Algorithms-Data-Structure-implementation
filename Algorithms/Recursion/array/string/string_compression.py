from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0    
        n = len(chars)

        while read < n:
            current_char = chars[read]
            count = 0

            # Count occurrences of the current character
            while read < n and chars[read] == current_char:
                read += 1
                count += 1

            # Write the current character
            chars[write] = current_char
            write += 1
            print(f"Current character: {current_char}, Count: {count}")
            print(f"Chars after writing character: {chars[:write]}")

            # Write the count if more than 1
            if count > 1:
                for ch in str(count):
                    chars[write] = ch
                    write += 1
                print(f"Chars after writing count: {chars[:write]}")

        # Return the new length of the compressed array
        return write

# Testing the solution
solution = Solution()

# Direct test cases
print(solution.compress(['a','a','b','b','c','c','c']))  # Expected output: 6, compressed array: ['a', '2', 'b', '2', 'c', '3']
print(solution.compress(['a'] * 12))  # Expected output: 3, compressed array: ['a', '1', '2']

# Multiple test cases
test_cases = [
    (['a', 'a', 'b', 'b', 'c', 'c', 'c'], 6, ['a', '2', 'b', '2', 'c', '3']),
    (['a'], 1, ['a']),
    (['a'] * 12, 3, ['a', '1', '2']),
    (['a', 'b', 'b', 'c', 'c', 'c', 'd'], 6, ['a', 'b', '2', 'c', '3', 'd']),
    (['a'] * 100, 4, ['a', '1', '0', '0']),
    (['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c'], 6, ['a', '4', 'b', '4', 'c']),
    (['x', 'y', 'y', 'y', 'z'], 5, ['x', 'y', '3', 'z']),
]

for idx, (chars_input, expected_length, expected_output) in enumerate(test_cases):
    chars = chars_input.copy()  # Copy to avoid modifying the original test case
    result_length = solution.compress(chars)
    result_output = chars[:result_length]
    print(f"Test Case {idx + 1}:")
    print(f"Input: {chars_input}")
    print(f"Expected Length: {expected_length}, Actual Length: {result_length}")
    print(f"Expected Output: {expected_output}, Actual Output: {result_output}")
    print(f"Test {'Passed' if result_length == expected_length and result_output == expected_output else 'Failed'}\n")
