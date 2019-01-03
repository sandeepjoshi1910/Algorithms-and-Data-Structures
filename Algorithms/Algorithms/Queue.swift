

// Created by Sandeep Joshi on 06/17/2018
// Implementation of Queue in Swift


class Queue {
    var head: Node?

    func enqueue(value: Int) {
        let new_node = Node(data: value)
        

        if head?.data != nil {
            new_node.next = head
            head = new_node
        } else {
            head = Node(data: value)
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
