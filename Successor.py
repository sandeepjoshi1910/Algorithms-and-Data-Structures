"""
    Question 4.6: Successor: Write an algorithm to find the "next" node (i .e., in-order successor) of a given node in a
    binary search tree. You may assume that each node has a link to its parent.

"""

class TNode:

    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
        self.parent = None
        self.next = None

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
                new_node = TNode(data)
                new_node.parent = node
                node.right = new_node
                return
            
        else:
            if node.left != None:
                self.addData(data,node.left)
            else:
                new_node = TNode(data)
                new_node.parent = node
                node.left = new_node
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

    def add_next_links(self):

        que = []
        node_list = []
        que.append(self.root)

        while len(que) > 0:
            node = que.pop(0)
            node_list.append(node)

            if node.left != None:
                que.append(node.left)

            if node.right != None:
                que.append(node.right)

        while len(node_list) > 0:
            if len(node_list) == 1:
                break
            
            if node_list[0].parent == None:
                node_list.pop(0)
                continue
            
            else:
                if (node_list[0].parent == node_list[1].parent) or (node_list[0].parent.next == node_list[1].parent):
                    node_list[0].next = node_list[1]
                    node_list.pop(0)
                else:
                    node_list.pop(0)

    def get_next_link_for_node(self,value):
        self.add_next_links()
        que = []
        que.append(self.root)

        while len(que) > 0:
            node = que.pop(0)
            if node.data == value:
                if node.next == None:
                    return -1
                else:
                    return node.next.data
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
        return -1


nums = [20,10,30,5,15,25,35,1,7,11,16,22,27,34]

t = Tree()

for num in nums:
    t.addData(num,t.root)

print(t.get_next_link_for_node(7))