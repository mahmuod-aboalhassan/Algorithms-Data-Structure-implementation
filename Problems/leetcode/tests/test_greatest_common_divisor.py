from leetcode.greatest_common_divisor import Solution
solution=Solution()
def test_examples():
    # Simple Test Cases Before Submitting Solution 
    assert solution.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert solution.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert solution.gcdOfStrings("LEET", "CODE") == ""
