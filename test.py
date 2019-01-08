class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        def getArea(container):
            container[0] = container[-1] = min(container[0] ,container[-1])
            total = (len(container) - 2) * max(container)
            for i in range(1,len(container)-1):
                total = total - container[i]
            return total
            
        
        i = 0
        l = 0
        r = 0
        conts = []
        
        while i < len(height):
            if i == 0 and height[i] == 0:
                i = i + 1
                l = l + 1
                continue


            if l != i and height[i] < height[l]:
                i = i + 1
                continue

            elif l == i:
                i = i + 1
                continue

            elif l != i and height[i] >= height[l]:
                if i + 1 <= len(height) - 1:
                    if height[i+1] < height[i]:
                        if (l,i) not in conts:
                            conts.append((l,i))
                        l = i
                    else:
                        i = i + 1
                else:
                    if (l,i) not in conts:
                        conts.append((l,i))
                    i = i + 1

            elif l < i and height[i] < height[l]:
                i = i + 1
                
        print(conts)

s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])