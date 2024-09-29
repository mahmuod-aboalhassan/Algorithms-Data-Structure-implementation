class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first,second=0,0
        n1=len(t)
        n2=len(s)
        while second<n2 and first<n1:
            if t[first]==s[second]:
                second+=1
                first+=1
            else:
                first+=1
        return False if second<n2 else True