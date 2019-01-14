class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if nums == []:
            return True
        
        Sum = sum(nums)

        if Sum %2 != 0:
            return False
        
        half = int(Sum / 2)
        halflen = int(len(nums)/2)
        if half in nums:
            return True
        
        # subsets = []
        subs = []
        
        for it, num in enumerate(nums):
            subs.append(([num],it,num))
        sublen = 1
        while True:
            nextsubs = []
            
            for subset in subs:
                for it,num in enumerate(nums[subset[1]+1:]):
                    sub = subset[0] + [num]
                    nextsubs.append((sub,it+1,subset[2]+num))
                    if len(sub) > sublen:
                        sublen = len(sub)
                    if subset[2]+num == half:
                        return True
            # subsets.append(subs)
            print(sublen)
            subs = nextsubs
            if sublen >= halflen:
                return False

s = Solution()
print(s.canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]))