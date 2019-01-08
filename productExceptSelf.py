# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        f = 1
        b = 1
        i = 0
        j = len(nums)-1
        fr = {}
        br = {}
        while i <= len(nums)-1 and j >= 0:
            f = f * nums[i]
            b = b * nums[j]
            fr[i] = f
            br[j] = b
            i = i + 1
            j = j - 1
        print(fr)
        print(br)
        ans = []
        for i in range(0,len(nums)):
            if i == 0:
                ans.append(br[i+1])
            elif i == len(nums)-1:
                ans.append(fr[i-1])
            else:
                ans.append(fr[i-1]*br[i+1])
                
        return ans