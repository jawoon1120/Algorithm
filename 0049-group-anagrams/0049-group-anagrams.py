from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_index_dict = defaultdict(list)
        for index, single_str in enumerate(strs):
            anagrams_index_dict[''.join(sorted(single_str))].append(index)
        
        result = [
            [strs[index] for index in index_list] 
            for key, index_list in anagrams_index_dict.items()
        ] 

        return result
        