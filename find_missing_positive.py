class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        
        snum = set(nums)
        
        if 1 not in snum:
            return 1
        
        ans = None
        for e in snum:
            if e+1 not in snum and e+1 > 0:
                if ans == None:
                    ans = e+1
                elif e+1 < ans:
                    ans = e+1
        return ans
                    