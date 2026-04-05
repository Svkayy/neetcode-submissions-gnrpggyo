class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            s = "".join(sorted(string))
            hashmap[s].append(string)
        
        return list(hashmap.values())