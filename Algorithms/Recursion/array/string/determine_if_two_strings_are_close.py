class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def compare_dicts(d1,d2):
            l1=sorted(list(d1.values()))
            l2=sorted(list(d2.values()))
            return l1==l2
        if len(word1)!= len(word2):
            return False
        if set(word1)!=set(word2):
            return False
        
        d1={}
        d2={}
        for i in word1:
            d1[i]=d1.get(i,0)+1
        for i in word2:
            d2[i]=d2.get(i,0)+1
        # print(dict_one,dict_two)
        print(d1,d2)
        return compare_dicts(d1,d2)

