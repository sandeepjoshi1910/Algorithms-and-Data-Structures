


class Node(object):

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.next_node

    def setData(self, data):
        self.data = data

    def setNext(self, next_node):
        self.next_node = next_node

    def noOfnodesInList(self):
        noOfNodes = 1
        currentNode = self
        while currentNode.next_node != None:
            noOfNodes = noOfNodes + 1
            currentNode = currentNode.next_node

        return noOfNodes




class List(object):

    head = None
    tail = None
    size = 0

    def insert(self, data: object) -> object:

        if self.head == None:
            self.head = self.tail = Node(data)

        tempNode = self.head
        self.head = Node(data)
        self.head.next_node = tempNode

        self.size = self.size + 1


    def getSize(self):
        return self.size

    def printAllNodes(self):
        currentNode = self.head
        while currentNode.next_node != None:
            print(currentNode.data)
            currentNode = currentNode.next_node



nums = List()
nums.insert(10)
nums.insert(20)
nums.insert(30)
nums.insert(40)
nums.printAllNodes()










