#https://leetcode.com/problems/subsets/submissions/
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        ans = []
        for num in nums:
            ans.append([num])
            
        subs = ans
        while len(subs)!=1:
            nex = []
            for sub in subs:
                shouldapp = False
                for num in nums:
                    if not shouldapp and num == sub[-1]:
                        shouldapp = True
                        
                    
                    elif shouldapp:
                        nex.append(sub+[num])
            [ans.append(x) for x in nex]
            subs = nex
        ans.append([])
        return ans


s = Solution()
print(s.subsets([1,2,3,4]))