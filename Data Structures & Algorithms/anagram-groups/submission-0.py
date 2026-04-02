class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrings = []
        for string in strs:
            sortedStrings.append("".join(sorted(string)))
        
        seen = {}
        for i, s in enumerate(sortedStrings):
            if s in seen:
                seen[s].append(strs[i])
            else:
                seen[s] = [strs[i]]
                
        result = []
        for s in seen:
            result.append(seen[s])
        return result
