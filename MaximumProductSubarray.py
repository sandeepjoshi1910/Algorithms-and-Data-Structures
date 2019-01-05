# Problem on Leetcode : https://leetcode.com/problems/maximum-product-subarray/

# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        ans = None
        
        replacedone = False
        replacedtwoone = False
        
        n = []
        
        for i in range(0,len(nums)):
            if nums[i] != 1:
                n.append(nums[i])
            else:
                replacedone = True
        
        nums = n
        if nums == []:
            return 1
        
        n = []
        i = 0
        while i < len(nums):
            if nums[i] == -1:
                if i != len(nums)-1:
                    if nums[i+1] == -1:
                        i = i + 2
                        replacedtwoone = True
                        continue
            n.append(nums[i])
            i = i + 1
                
        nums = n
        
        if nums == []:
            return 1
        
        print(nums)
        for i in range(0,len(nums)):
            pr = 1 
            prev = None
            for j in range(i,len(nums)):
                pr = pr * nums[j]
               
                if ans == None:
                    ans = pr
                if pr > ans:
                    ans = pr

        if ans <= 0 :
            if replacedone == True or replacedtwoone == True:
                ans = 1
        return ans