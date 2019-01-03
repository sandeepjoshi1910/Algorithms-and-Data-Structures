class Node:

    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

    def insert(self,data):

        if self.root == None:
            self.root = Node()
            self.root.value = data
            return
        
        node  = self.root

        while node != None:
            if data <= node.value:
                if node.left != None:
                    node = node.left
                    continue
                else:
                    node.left = Node()
                    node.left.value = data
                    break
            else:
                if node.right != None:
                    node = node.right
                    continue
                else:
                    node.right = Node()
                    node.right.value = data
                    break

        
    def inorder(self,node):
        if node.left == None and node.right == None:
            print(node.value)
            return
        
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

    def preorder(self,node):
        if node == None:
            return
        
        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)

    def get_min_depth(self):
        cur = []
        nex = []
        level = 0
        cur.append(self.root)

        while True:
            for elem in cur:
                if elem.left == None and elem.right == None:
                    return (level + 1)
                if elem.left != None:
                    nex.append(elem.left)
                if elem.right != None:
                    nex.append(elem.right)
            
            level = level + 1
            cur = nex[:]
            nex = []


t = Tree()

nums = [20,10,30,5,15,25,35]

for num in nums:
    t.insert(num)

t.preorder(t.root)
        
print("Minimum depth of the tree: " + str(t.get_min_depth()))