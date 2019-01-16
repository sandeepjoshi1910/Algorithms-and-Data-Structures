# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = -1
        end = -1
        
        for it,num in enumerate(nums):
            if num == target and start == -1:
                start = it
                end = it
            elif num == target:
                end = it
        return [start,end]