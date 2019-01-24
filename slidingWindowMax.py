# https://leetcode.com/problems/sliding-window-maximum/
# Sliding window maximum

import heapq
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return []
        elif nums != [] and k == 1:
            return nums
        output = []
        
        l = 0
        r = k
        maxv = None
        
        while r <= len(nums):
            arr = nums[l:r]
            heapq.heapify(arr)
            output.append(heapq.nlargest(1,arr)[0])
            l = l + 1
            r = r + 1
        return output