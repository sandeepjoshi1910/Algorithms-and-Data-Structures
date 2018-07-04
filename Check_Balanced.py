"""
    Question 4.4: Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
    this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
    node never differ by more than one.
"""

class TNode:

    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
        self.num_nodes_in_subtree = 0
        self.num_nodes_in_left_subtree = 0
        self.num_nodes_in_right_subtree = 0

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
    

    def compute_subtree_length(self,node):

        if node.left == None and node.right == None:
            return 0

        left_num = None
        right_num = None
        if node.left != None:
            left_num = self.compute_subtree_length(node.left)
        if node.right != None:
            right_num = self.compute_subtree_length(node.right)
        
        if left_num != None:
            node.num_nodes_in_left_subtree = node.num_nodes_in_left_subtree + 1 + left_num

        if right_num != None:
            node.num_nodes_in_right_subtree = node.num_nodes_in_right_subtree + 1 + right_num

        return node.num_nodes_in_left_subtree + node.num_nodes_in_right_subtree


    def is_tree_balanced(self):
        self.compute_subtree_length(self.root)

        que = []
        que.append(self.root)

        while len(que) != 0:
            node = que.pop(0)
            if abs(node.num_nodes_in_left_subtree - node.num_nodes_in_right_subtree) > 1:
                return False
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
        
        return True


    



nums = [20,10,30,5,15,25,35,1,7,11,16,22,27,34]

t = Tree()

for num in nums:
    t.addData(num,t.root)


# t.inorder(t.root)

print(t.is_tree_balanced())
