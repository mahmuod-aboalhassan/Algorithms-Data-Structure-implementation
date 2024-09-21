
# reverse String using Recursion and two pointers technique 
class Solution(object):
    def reverseString(self, s):
        left,right=0,len(s)-1
        def reverse(s,right,left):
            if right<left:
                return 0 
            # print(s)
            s[left],s[right]=s[right],s[left]
            return reverse(s,right-1,left+1)
        reverse(s,right,left)