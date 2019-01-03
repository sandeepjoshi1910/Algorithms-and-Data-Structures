class Solution:
    
    def createAdlists(self,edges):
        """
        :type edges: List[List[int]]
        :rtype: dict
        """
        alist = {}
        
        for edge in edges:
            for i in range(0,2):
                if edge[i] in alist.keys():
                    alist[edge[i]].append(edge[1-i])
                else:
                    alist[edge[i]] = [edge[1-i]]
        return alist        
    
    def dist(self,i,j,alist):
        q = []
        seen = []
        dist = 0
        children = [i]
        while True:
            q = children.copy()
            children = []
            for node in q:
                seen.append(node)
                if j not in alist[node]:
                    for ele in alist[node]:
                        if ele not in seen:
                            children.append(ele)
                else:
                    return dist+1
            dist = dist + 1
            
        
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        alist = self.createAdlists(edges)
        
        distances = {}
        for i in range(0,N):
            ans = 0
            li = list(range(0,N))
            li.remove(i)
            for j in li:
                ans = ans + self.dist(i,j,alist)
            distances[i] = ans
        return list(distances.values())
                

s = Solution()
print(s.sumOfDistancesInTree(100,[[33,17],[60,96],[5,11],[11,91],[17,83],[36,61],[47,40],[32,22],[14,56],[4,85],[64,30],[2,21],[77,49],[44,77],[72,19],[89,24],[58,93],[94,54],[71,45],[14,32],[83,52],[6,80],[6,99],[23,56],[81,5],[6,54],[56,5],[44,45],[68,62],[75,16],[32,9],[97,15],[92,87],[99,65],[45,99],[45,46],[6,97],[14,0],[67,93],[73,95],[73,7],[3,69],[29,88],[51,85],[71,50],[19,14],[2,46],[37,6],[41,79],[95,45],[84,38],[53,44],[80,27],[43,58],[30,26],[25,47],[13,55],[46,93],[92,20],[14,10],[78,96],[98,27],[45,57],[1,80],[62,42],[51,93],[13,69],[37,34],[62,26],[8,41],[82,17],[76,63],[59,20],[38,6],[14,51],[76,2],[75,65],[70,28],[61,31],[32,86],[38,66],[63,39],[62,51],[99,31],[80,96],[92,26],[28,94],[56,74],[68,48],[47,51],[29,38],[79,58],[45,90],[54,3],[26,12],[35,68],[98,18],[45,17],[30,24]]))                