
class Node {
    var data: Int?
    var next: Node?
}

class Queue {
    var head: Node?

    func enqueue(value: Int) {
        let new_node = Node()
        new_node.data = value

        if head?.data != nil {
            new_node.next = head
            head = new_node
        } else {
            head = Node()
            head?.data = value
            head?.next = nil
        }
    }

    func dequeue() -> Int {
        var current: Node? = head

        while current?.next?.next != nil {
            current = current?.next
        }
        let data = (current?.next?.data)!
        current?.next = nil
        return data
    }
}


var q = Queue()
let nums = [1,2,3,4,5,6,7,8,9]
for num in nums {
    q.enqueue(value: num)
}

for _ in nums {
    print(q.dequeue())
}