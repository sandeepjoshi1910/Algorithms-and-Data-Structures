# Problem : Two Sum : https://leetcode.com/problems/two-sum/#/description
#
#   Description : Given an array of integers, return indices of the two numbers such that,
#   they add up to a specific target.
#   You may assume that each input would have exactly one solution,
#   and you may not use the same element twice.
#
#   Example:
#   Given nums = [2, 7, 11, 15], target = 9,
#   Because nums[0] + nums[1] = 2 + 7 = 9,
#   return [0, 1].

# Solution below :

class Solution(object):
    def twoSum(self, nums, target):
        indeces = []
        for i in range(0, len(nums)):
            expectedNum = target - nums[i]
            for j in range(0, len(nums)):
                if nums[j] == expectedNum and i!=j:
                    secondIndex = j
                    break
                else:
                    secondIndex = -1
            if secondIndex != -1:
                indeces.append(i)
                indeces.append(secondIndex)
                return indeces


sol = Solution()
indeces = sol.twoSum([-1,-2,-3,-4,-5],-8)
print(indeces)