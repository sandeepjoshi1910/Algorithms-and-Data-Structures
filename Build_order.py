"""
  Question 4.7: Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
                projects, where the second project is dependent on the first project). All of a project's dependencies
                must be built before the project is. Find a build order that will allow the projects to be built. If there
                is no valid build order, return an error.
                EXAMPLE
                Input:
                projects: a, b, c, d, e, f
                dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
                Output: f, e, a, b, d, c

"""

class graph:

    def __init__(self):
        self.graph = {}

    def addEdge(self,a,b):
        if b in self.graph.keys():
            self.graph[b].append(a)
        else:
            self.graph[b] = [a]

    def generate_build_order(self,projs):
        build_order = []

        que = []
        for pro in projs:
            if pro not in self.graph.keys() and pro not in self.graph.values():
                build_order.append(pro)
                projs.remove(pro)
        
        while True:

            if len(list(self.graph.keys())) == 0:
                break
            for proj in projs:
                
                if len(list(self.graph.keys())) == 0:
                    break

                if proj in build_order:
                    continue

                que = []
                que.append(proj)
                while len(que) > 0:
                    pr = que.pop(0)

                    if pr not in self.graph.keys() and (pr not in build_order):
                        for key in self.graph.keys():
                            if pr in self.graph[key]:
                                self.graph[key].remove(pr)
                        build_order.append(pr)
                        break
                    elif self.graph[pr] == []:
                        for key in self.graph.keys():
                            if pr in self.graph[key]:
                                self.graph[key].remove(pr)
                        del self.graph[pr]
                        build_order.append(pr)
                        break
                    else:
                        for project in self.graph[pr]:
                            que.append(project)

        return build_order
            

            


g = graph()

g.addEdge('a','d')
g.addEdge('f','b')
g.addEdge('b','d')
g.addEdge('f','a')
g.addEdge('d','c')

print(g.generate_build_order(['a','b','c','d','e','f']))

print(g.graph)