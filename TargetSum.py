# https://leetcode.com/problems/target-sum/
class Solution:
    
    memo = {}
    
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if nums == []:
            return 0

        self.memo = {}
        return self.targetSum(nums,S,0,0)
        
        
    def targetSum(self,nums,S,Sum,pos):
        if (pos,Sum) in self.memo:
            return self.memo[(pos,Sum)]
        
        if pos == len(nums) - 1:
            if nums[pos] + Sum == S and Sum - nums[pos] == S:
                return 2
                
            elif Sum - nums[pos] == S:
                return 1
                
            elif nums[pos] + Sum == S:
                return 1
            else:
                return 0
        
        ans1 = self.targetSum(nums,S,Sum+nums[pos],pos+1)
        ans2 = self.targetSum(nums,S,Sum-nums[pos],pos+1)
        
        
        self.memo[(pos,Sum)] = ans1 + ans2
        return self.memo[(pos,Sum)]