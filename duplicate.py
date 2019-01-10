class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numbers = set()
        
        for num in nums:
            if num in numbers:
                return num
            else:
                numbers.add(num)
                
s = Solution()
s.findDuplicate([1,1])