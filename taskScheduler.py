class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskdict = {}
        for task in tasks:
            if task not in taskdict:
                taskdict[task] = 1 
            else:
                taskdict[task] += 1
        
        # keys = sorted(taskdict,key=taskdict.get,reverse=False)
        keys = list(taskdict.keys())
        
        schedule = []
        posdict = {}
        for key in keys:
            posdict[key] = -1
            
        while keys != []:
            
            for key in keys:
                
                if posdict[key] == -1:
                    schedule.append(str(key))  
                    taskdict[key] -= 1
                    posdict[key] = len(schedule)-1
                
                elif len(schedule) - posdict[key] <= n:
                    numid = n - (len(schedule)-posdict[key]-1)
                    schedule = schedule + ["idle"] * numid
                    schedule.append(str(key))
                    posdict[key] = len(schedule)-1
                    taskdict[key] -= 1
                
                elif len(schedule) - posdict[key] > n:
                    schedule.append(str(key))
                    posdict[key] = len(schedule)-1
                    taskdict[key] -= 1
                
            for key in keys:
                if taskdict[key] == 0:
                    del taskdict[key]
            
            keys = list(taskdict.keys())
        print(schedule)
        return len(schedule)

s = Solution()
s.leastInterval(["A","A","A","B","B","B","C"],4)        