from leetcode.merge_two_string_alternately import Solution

solution = Solution()

def test_examples():
    assert solution.mergeAlternately('abc','pqr')=='apbqcr'
    assert solution.mergeAlternately('ab','pqrs')== 'apbqrs'
    assert solution.mergeAlternately('abcd','pq')=='apbqcd'