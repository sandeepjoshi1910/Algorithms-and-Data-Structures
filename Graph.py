
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

    def DFSearch(self):
        self.visited = []
        self.DFS(list(self.graph.keys())[0])

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





    
g = Graph()

g.addEdge(1,3)
g.addEdge(2,1)
g.addEdge(3,2)
g.addEdge(3,4)
g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(0,5)
g.addEdge(1,4)


g.DFSearch()

g.BFSearch()
    