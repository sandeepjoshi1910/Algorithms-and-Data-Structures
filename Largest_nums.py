class Solution:
    
    memo = {}
    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        self.memo = {}
        
        ans = self.get_largest(sorted(nums))
        # print(self.memo)
        print(ans)
        return ans
        
    def get_largest(self,nums):
        
        if set(nums) in list(self.memo.keys()):
            return self.memo[set(nums)]
        
        if len(nums) == 2:
            a = str(nums[0])+str(nums[1])
            b = str(nums[1])+str(nums[0])
            
            if a > b:
                return a
            elif a < b:
                return b
            else:
                return a    
        
        ans = []
        
        for i in range(0,len(nums)):
            num1 = int(self.get_largest(nums[0:i]))
            num2 = int(self.get_largest(nums[i+1:]))    
            ans.append(str(nums[i])+self.get_largest([num2]))
            
        if ans == []:
            return 0

        self.memo[tuple(nums)] = max(ans)
        print(self.memo)
        ans.remove([])
        return max(ans)


s = Solution()
s.largestNumber([1,2,3,4,5,6,7,8,9,0])        