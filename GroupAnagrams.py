# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        if strs == []:
            return []
        elif len(strs) == 1:
            return [strs]
        
        sortstrs = []
        [sortstrs.append(''.join(sorted(s))) for s in strs]
        
        count_dict = {}
        
        for it,s in enumerate(sortstrs):
            if s in count_dict:
                count_dict[s].append(it)
            else:
                count_dict[s] = [it]
                
        ans = []
        
        for k,v in count_dict.items():
            ans.append([strs[i] for i in v])
            
        return ans