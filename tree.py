

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
        

nums = [10,4,1,12,3,9,5,6]

t = Tree()

for num in nums:
    t.addData(num,t.root)

t.inorder(t.root)