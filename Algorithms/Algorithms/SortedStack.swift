
/*

CTCI Question 3.5:

Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

*/




class Node {
    var data: Int?
    var next: Node?
    
    init(data: Int) {
        self.data = data
        self.next = nil
    }
}

class Stack {
    
    var head: Node? = nil
    
    func push(value: Int) {
        if head == nil {
            head = Node(data: value)
        } else {
            let new_node = Node(data: value)
            new_node.next = head
            head = new_node
        }
    }
    
    func pop() -> Int {
        if self.head == nil {
            return -1
        }
        let data = (head!.data)!
        head = head!.next
        return data
    }
    
    func peek() -> Int {
        if head == nil {
            return -1
        }
        
        return (head!.data)!
    }
    
    func printStack() {
        var current: Node? = head! as Node?
        print("Stack Print")
        while current != nil {
            print(current!.data!)
            current = current!.next
        }
    }
}


class SortedStack {
    var mainStack: Stack?
    var helperStack: Stack?
    
    init() {
        self.mainStack = nil
        self.helperStack = nil
        
    }
    
    func push(value: Int) {
        
        if self.mainStack == nil {
            self.mainStack = Stack()
            self.helperStack = Stack()
            self.mainStack!.push(value: value)
            return
        }
        
        while true {
            
            let topVal = self.mainStack!.peek()
            
            if topVal == -1 {
                break
            }
            
            if topVal <= value {
                let poppedVal = self.mainStack!.pop()
                self.helperStack!.push(value: poppedVal)
            } else {
                break
            }
        }
        
        self.mainStack!.push(value: value)
        
        while (self.helperStack!.peek()) != -1 {
            let val = (self.helperStack!.pop())
            self.mainStack!.push(value: val)
        }
        
    }
    
    func printSortedStack() {
        self.mainStack!.printStack()
    }
    
}

/*
var ss = SortedStack()

let nums = [10, 3, 12, 7, 2, 11, 9]

for num in nums {
    ss.push(value: num)
}

ss.printSortedStack()

*/


/*
Output:

Stack Print
2
3
7
9
10
11
12


*/
