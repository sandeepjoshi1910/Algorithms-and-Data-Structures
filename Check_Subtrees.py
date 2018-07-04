"""

    Check Subtree:  Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
                    algorithm to determine if T2 is a subtree of Tl.
                    A tree T2 is a subtree ofTi if there exists a node n in Ti such that the subtree of n is identical to T2.
                    That is, if you cut off the tree at node n, the two trees would be identical.

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

    def inorder(self,node,tr_list):
        if node.left == None and node.right == None:
            tr_list.append(node.data)
            return tr_list
        if node.left != None:
            self.inorder(node.left,tr_list)
        tr_list.append(node.data)
        if node.right != None:
            self.inorder(node.right,tr_list)
        return tr_list


def is_subtree(list1, list2):
    if all(elem in list2  for elem in list1):
        return True
    else:
        return False


nums1 = [20,15,25]
nums2 = [10,5,3,7,20,15,25]

t1 = Tree()
t2 = Tree()

for num in nums1:
    t1.addData(num,t1.root)

for num in nums2:
    t2.addData(num,t2.root)



list1 = t1.inorder(t1.root,[])




list2 = t2.inorder(t2.root,[])

print(is_subtree(list1,list2))