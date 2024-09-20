# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# 
# Return the merged string.
# 
#  
# 
# Example 1:
# 
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
# 
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:
# 
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
# 

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_str=''
        i,j=0,0
        n1,n2=len(word1),len(word2)

        while i<n1 and j<n2:

            # print(i,j)
            # print(word1,word2)
            char1=word1[0]
            char2=word2[0]
            word1=word1[1:]
            word2=word2[1:]
            # print('wording after splitting')
            # print(word1,word2)
            i+=1
            j+=1
            merged_str+=char1+char2
            # print(i,j)
        return merged_str+word1+word2
        