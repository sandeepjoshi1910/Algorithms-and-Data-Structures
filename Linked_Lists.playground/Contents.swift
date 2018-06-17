import Cocoa

/*
# Linked List problems from CTCI
*/

/*
 Q1 : Write code to remove duplicates from an unsorted linked list
 Follow up: How would you solve this problem if a temporary buffer is not allowed?
 */

class Node {
    var data : Int?
    var next : Node?
    
    init(val: Int) {
        self.data = val
        self.next = nil
    }
}

class Llist {
    
    var head : Node?
    
    func insertNode(value: Int) {
        var current = self.head
        while  current?.next != nil{
            current = current?.next
        }
        let newNode = Node(val: value)
        current?.next = newNode
    }
    
    func printList() {
        var current : Node? = self.head
        
        while current != nil {
            print(current?.data as! Int)
            current = current?.next
        }
    }
    
    func insertValuesFrom(values: [Int]) {
        for val in values {
            self.insertNode(value: val)
        }
    }
}


let values : [Int] = [2,5,7,2,4,9,10,5,11,16]
    
let list: Llist = Llist()

list.insertValuesFrom(values: values)

list.printList()







