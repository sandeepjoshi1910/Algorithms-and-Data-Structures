"""
    Question 4.9:   BST Sequences: A binary search tree was created by traversing through an array from left to right
                    and inserting each element. Given a binary search tree with distinct elements, print all possible
                    arrays that could have led to this tree.

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

    def get_BST_Sequences(self,node):

        if node.left == None and node.right == None:
            return []
        
        left_lists = self.get_BST_Sequences(node.left)
        right_lists = self.get_BST_Sequences(node.right)

        if left_lists == [] and right_lists == []:
            return [ [node.data, node.left.data, node.right.data], [node.data, node.right.data, node.left.data]]
        
        main_lists = []

        for left_list in left_lists:
            for right_list in right_lists:
                main_lists.append([node.data]+left_list+right_list)
        
        for right_list in right_lists:
            for left_list in left_lists:
                main_lists.append([node.data]+right_list+left_list)


        return main_lists


nums = [10, 4, 2, 5, 20, 15, 25]

t = Tree()

for num in nums:
    t.addData(num,t.root)

print(len(t.get_BST_Sequences(t.root)))