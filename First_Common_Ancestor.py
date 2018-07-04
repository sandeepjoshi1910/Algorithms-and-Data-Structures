"""
    Question: 4.8: First Common Ancestor: Design an algorithm and write code to find the first common ancestor
                   of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
                   necessarily a binary search tree.
"""

class TNode:

    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

    def addData(self,data,node):
        if node == None:
            self.root = TNode(data)
            return
        
        if data > node.data:
            if node.right != None:
                self.addData(data,node.right)
            
            else:
                node.right = TNode(data)
                return
            
        else:
            if node.left != None:
                self.addData(data,node.left)
            else:
                node.left = TNode(data)
                return

    def inorder(self,node):
        if node.left == None and node.right == None:
            print(node.data)
            return
        if node.left != None:
            self.inorder(node.left)
        print(node.data)
        if node.right != None:
            self.inorder(node.right)

    def first_common_ancestor(self,val1,val2):
        traversal,_  = self.depth_traversal(val1,self.root,[],False)
        traversal2,_  = self.depth_traversal(val2,self.root,[],False)

        traversal.reverse()
        traversal2.reverse()

        if traversal[0] != traversal2[0]:
            return False
        
        fca = -1

        for i in range(0,len(traversal)):
            if traversal[i] == traversal2[i]:
                fca = traversal[i]
            else:
                break
        
        return fca

    def depth_traversal(self,val,node,trail,should_capture):
        if node.data == val:
            trail.append(node.data)
            return trail, True
        
        if node.left != None:
            trail, should_capl = self.depth_traversal(val,node.left,trail,should_capture)
            if should_capl == True:
                trail.append(node.data)
                return trail, should_capl

        if node.right != None:
            trail, should_capr = self.depth_traversal(val,node.right,trail,should_capture)
            if should_capr == True:
                trail.append(node.data)
                return trail, should_capr

        return [], False



nums = [20,10,30,5,15,25,35,1,7,11,16,22,27,34,36]


t = Tree()

for num in nums:
    t.addData(num,t.root)

# t.inorder(t.root)
print(t.first_common_ancestor(16,11))