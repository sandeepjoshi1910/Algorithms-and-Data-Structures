
/* 
Question 3.3 : Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).
*/


// Assumption: Max size of each stack is 5

class Node {
    var data: Int?
    var next: Node?
}

class Stack {
    
    var top: Node? = nil
    var size: Int = 0
        
    func push(value: Int) {
        
        let new_node = Node()
        new_node.data = value
        new_node.next = top
        top = new_node
        self.size = self.size + 1
        // print("Pushed")
    }
    
    func peek()->Int {
        return top!.data!
    }

    func pop()->Int {
        let data: Int?
        if top!.data != nil {
            data = top!.data!        
            self.size = self.size - 1
        } else {
            data = -1
        }

        if top!.next != nil {
            top = top!.next
            
        } else {
            top!.data = nil
        }
        
        return data!
    }
    
    func printStack() {
        var current: Node? = top! as Node?
        print("Stack Print")
        while current != nil {
            print(current!.data!)
            current = current!.next
        }
    }
}

class SetOfStacks {

    var stacks: [Stack] = []

    func push(value: Int) {
        var stack: Stack?
        if self.stacks.isEmpty {
            stack = Stack()
            self.stacks.append(stack!)
        } else if self.stacks.last!.size == 5 {
            stack = Stack()
            self.stacks.append(stack!)
        } else {
            stack = self.stacks.last!
        }

        stack!.push(value: value)

    }

    func pop() -> Int {
        // Check if the stacks is empty
        if self.stacks.isEmpty {
            return -1
        }

        let data = self.stacks.last!.pop()
        
        if self.stacks.last!.size == 0 {
            print("Removing empty stack from stacks")
            self.stacks.removeLast()
        }

        return data
    }

    func printStacks() {
        if self.stacks.isEmpty {
            print("Set of Stacks is empty")
            return
        }
        for stack in self.stacks {
            stack.printStack()
        }
    }
}

let s = SetOfStacks()

let nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for num in nums {
    s.push(value: num)
}

s.printStacks()

print("Popping the Set of stacks")

for _ in nums {
    print(s.pop())
}

print("Printing stacks again")
s.printStacks()

