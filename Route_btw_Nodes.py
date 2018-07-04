

"""
    Question 4.1: Route between the nodes:
    Given a directed graph, design an algorithm to find out whether there is a
    route between two nodes.

    Solution:
    Do a BFS and start with first node. If not found, again do a BFS now with second node
    So in directed graph, 0 -> 1, if you start with 1, you won't find a path unless there is
    another path through more nodes between 1 and 0. So we again try from 0 to find a path between 
    0 and 1
"""

class Graph:
    
    def __init__(self):
        self.graph = {}
        self.visited = []

    def addEdge(self,a,b):
        if a in self.graph.keys():
            self.graph[a].append(b)
        else:
            self.graph[a] = [b]

    def DFS(self,root):
        if root == None:
            return
        
        if root not in self.visited:
            print(root)
            self.visited.append(root)
        else:
            return
        
        if root in self.graph.keys():
            for i in self.graph[root]:
                self.DFS(i)

    def DFSearch(self,start):
        self.visited = []
        self.DFS(start)

    def BFSearch(self):
        self.visited = []
        self.BFS()


    def BFS(self):
        que = []
        que.append(list(self.graph.keys())[0])

        while len(que) != 0:
            node = que.pop(0)
            if node not in self.visited:
                print(node)
                self.visited.append(node)
            if node in self.graph.keys():
                for i in self.graph[node]:
                    if i not in self.visited:
                        que.append(i)
    
    def route_bet_nodes(self,node1,node2):
        self.visited = []
        if self.find_nodes(node1,node2) == False:
            self.visited = []
            if self.find_nodes(node2,node1) == False:
                return False
            else:
                return True
        else:
            return True

    def find_nodes(self,node1,node2):
        que = []
        que.append(node1)

        while len(que) != 0:
            node = que.pop(0)
            if node not in self.visited:
                self.visited.append(node)
                if node == node2:
                    return True
                if node in self.graph.keys():
                    for i in self.graph[node]:
                        que.append(i)
        return False


g = Graph()
g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(0,5)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(3,2)
g.addEdge(3,4)
g.addEdge(2,1)

print(g.route_bet_nodes(2,5))