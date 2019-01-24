class Solution:
    memo = {}
    used = 0
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        self.memo = {}
        self.used = 0
        self.maxc(nums)
        print(self.used)
        return self.memo[tuple(nums)]
        
    def maxc(self,nums):
        
        if len(nums) == 1:
            return nums[0]
        
        if tuple(nums) in self.memo:
            self.used += 1
            print(self.used)
            return self.memo[tuple(nums)]
        
        ans = []
        
        for i in range(0,len(nums)):
            if i == 0:
                ans.append(nums[0]*nums[1] + self.maxc(nums[1:]))
            elif i == len(nums)-1:
                ans.append(nums[i-1]*nums[i] + self.maxc(nums[0:i]))
            else:
                ans.append(nums[i-1]*nums[i]*nums[i+1] + self.maxc(nums[0:i]+nums[i+1:]))
                
        self.memo[tuple(nums)] = max(ans)
        return max(ans)

s = Solution()
print(s.maxCoins([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]))