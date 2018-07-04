"""
    Question 4.3: List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).

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


    def get_depth_lists(self):
        que = []
        values = []
        que.append(self.root)

        while len(que) != 0:
            # list.pop(0) pops the first element
            node = que.pop(0)
            values.append(node.data)
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)

        num_nodes_in_level = 1
        level_lists = []

        while True:
            if len(values) >= num_nodes_in_level:
                level_list = values[0:num_nodes_in_level]
                level_lists.append(level_list)
                values = values[num_nodes_in_level:]
                num_nodes_in_level = num_nodes_in_level * 2
            else:
                level_lists.append(values)
                break

        print(level_lists)



nums = [10,4,1,12,3,9,5,6,14,71,33,24,62,20,74,21,82,16,15,11,45,23]

t = Tree()

for num in nums:
    t.addData(num,t.root)

t.get_depth_lists()

