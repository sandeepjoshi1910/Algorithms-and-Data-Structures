class Solution:
    memo = {}
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    
        ans,_ = self.csum(candidates,target)
        ans = [sorted(x) for x in ans]
        new_ans = []
        for i in ans:
            if i not in new_ans:
                new_ans.append(i)
        return  new_ans

    def csum(self,candidates,target):
        if target in self.memo.keys():
            return self.memo[target], True
        if target < 0:
            return [], False
        
        if target == 0:
            return [], True
        
        else:
            ans = []
            for candidate in candidates:
                sol, should_add = self.csum(candidates,target-candidate)
                if should_add:
                    if sol == []:
                        ans.append([candidate])
                    else:
                        [ans.append([candidate]+s) for s in sol]
                    
            if ans == []:
                return ans, False
            else:
                self.memo[target] = ans
                return ans, True

s = Solution()
print(s.combinationSum([2,3,5], 8))