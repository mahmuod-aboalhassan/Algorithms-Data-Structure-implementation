class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_of_occurrence={}
        for n in arr:
            dict_of_occurrence[n]=dict_of_occurrence.get(n,0)+1
        return  len(set(dict_of_occurrence.values()))== len(dict_of_occurrence.values())