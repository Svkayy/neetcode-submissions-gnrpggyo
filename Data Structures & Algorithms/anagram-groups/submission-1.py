class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
            
        sorted_strs = []
        for string in strs:
            sorted_strs.append("".join(sorted(string)))
        
        seen = defaultdict(list)
        for i, string in enumerate(sorted_strs):
            seen[string].append(strs[i])
        
        res = []
        for key in seen:
            res.append(seen[key])
        
        return res

