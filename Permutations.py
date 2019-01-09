# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]
        if len(nums) == 2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        
        ans = []
        for i in range(0,len(nums)):
            perms = self.permute(nums[0:i]+nums[i+1:])
            [ans.append(x+[nums[i]]) for x in perms]
                
        return ans