class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_str = ''
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)

        # Merge characters alternately while both strings have characters left
        while i < n1 and j < n2:
            merged_str += word1[i] + word2[j]
            i += 1
            j += 1

        # Add the remaining characters from either word1 or word2
        return merged_str + word1[i:] + word2[j:]
