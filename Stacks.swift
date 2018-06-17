class Stack {
    
    var top: Node?
        
    func push(value: Int) {
        
        let new_node = Node()
        new_node.data = value
        new_node.next = top
        top = new_node
    }
    
    func peek()->Int {
        return top!.data!
    }

    func pop()->Int {
        let data: Int? = top!.data!
        top = top!.next
        return data!
    }
    
    func printStack() {
        var current: Node? = top! as Node?
        while current != nil {
            print(current!.data!)
            current = current!.next
        }
    }
}


class Node {
    var data: Int?
    var next: Node?
}


var st = Stack()
st.push(value:5)
st.push(value:10)
st.push(value:12)
st.printStack()
print("\n")
print("Value popped: \(st.pop())")
st.printStack()
