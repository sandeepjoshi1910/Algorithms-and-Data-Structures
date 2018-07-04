
"""

    Question: 4.2: Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
    to create a binary search tree with minimal height.

"""


class Node:

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

    def construct_tree(self,arr):
        if arr == []:
            return
        mid = int(len(arr)/2)
        if self.root == None:
            self.root = Node()
            self.root.value = arr[mid]
            if len(arr) != 1:
                self.root.left = self.construct_tree(arr[:mid])
                self.root.right = self.construct_tree(arr[mid+1:])
            return self.root

        else:
            node = Node()
            node.value = arr[mid]
            if len(arr) != 1:
                node.left = self.construct_tree(arr[:mid])
                node.right = self.construct_tree(arr[mid+1:])
            return node

    def inorder(self,node):
        if node.left == None and node.right == None:
            print(node.value)
            return
        if node.left != None:
            self.inorder(node.left)
        print(node.value)
        if node.right != None:
            self.inorder(node.right)


t = Tree()
nums = [1,2,3,4,5,6,7,8]
t.construct_tree(nums)
t.inorder(t.root)