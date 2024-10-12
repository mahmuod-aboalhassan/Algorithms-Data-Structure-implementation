class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=set(nums1)
        n2=set(nums2)
        dif1=[]
        dif2=[]
        for ele in n1:
            if ele not in n2:
                dif1.append(ele)
        for ele in n2:
            if ele not in n1: 
                dif2.append(ele)
        return [dif1,dif2]