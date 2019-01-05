class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        if edges == []:
            return [0]
        def get_alist(edges):
            alist = {}
            for edge in edges:
                if edge[0] in alist.keys():
                    alist[edge[0]].append(edge[1])
                else:
                    alist[edge[0]] = [edge[1]]
                
                if edge[1] in alist.keys():
                    alist[edge[1]].append(edge[0])
                else:
                    alist[edge[1]] = [edge[0]]
            return alist
        
        alist = get_alist(edges)
        # print(alist)
        
        leaves = []
        treenodes = []
        distances = {}
        for key in alist.keys():
            if len(alist[key]) == 1:
                leaves.append(key)
            else:
                treenodes.append(key)
        
        # print(leaves,treenodes)
        if treenodes == []:
            treenodes = leaves
        
        nodes = list(range(0,n))
        
        
        prev = leaves
        dist = 1
        while nodes != []:
            print(nodes)
            nex = []
            nodestoremove = []
            for node in nodes:
                for n in prev:
                    if n in alist[node]:
                        if node in distances.keys():
                            distances[node][n] = dist
                        else:
                            distances[node] = {n:dist}
                        if node not in nex:
                            nex.append(node)
                        if node not in nodestoremove:
                            nodestoremove.append(n)
                        
            prev = nex
            dist = dist + 1
            for n in nodestoremove:
                if n in nodes:
                    nodes.remove(n)
        print(distances)

s = Solution()
s.findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])