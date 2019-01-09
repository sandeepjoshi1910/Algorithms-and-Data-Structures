# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        def bubbleSort(arr,k): 
            n = len(arr) 
            for i in range(0,k): 
                for j in range(0, n-i-1): 
                    if arr[j] > arr[j+1]: 
                        arr[j], arr[j+1] = arr[j+1], arr[j] 
        
        freq = {}
        
        for num in nums:
            if num in freq.keys():
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
        
        nums = list(freq.values())
        bubbleSort(nums,k)
        ans = []
        i = len(nums)-1
        print(nums)
        for i in range(len(nums)-1,len(nums)-1-k,-1):
            num = nums[i]
            for k,v in freq.items():
                if v == num and k not in ans:
                    ans.append(k)
        return ans