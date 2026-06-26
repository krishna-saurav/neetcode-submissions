class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict: dict[str,List[str]] = {}
        for ele in strs:
            anagram_key = str(sorted(ele))
            if anagram_key in anagram_dict.keys():
                anagram_dict[anagram_key] = anagram_dict.get(anagram_key,[]) + [ele]
            else:
                anagram_dict[anagram_key] = [ele]
        grouped_anagram=[anagram_group for anagram_group in anagram_dict.values() ] 
        return grouped_anagram
        