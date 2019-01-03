
/*

CTCI Question 3.6

Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked List data structure.

*/




class CNode {
    var data: String?
    var next: CNode?
    
    init(data: String) {
        self.data = data
        self.next = nil
    }
}

class CatDogList {
    var oldest: CNode?
    var latest: CNode?
    
    init() {
        self.oldest = nil
        
    }
    
    func enqueue(data: String) {
        if oldest == nil {
            self.oldest  = CNode(data: data)
            return
        }
        
        var current = self.oldest
        
        while current?.next != nil {
            current = current?.next
        }

        let new_node = CNode(data: data)
        current?.next = new_node
        
    }
    
    func dequeueAny() -> String {
        if oldest == nil {
            return "NO DATA"
        }
        
        let data = (self.oldest!.data)!
        
        self.oldest = self.oldest!.next
        
        return data
    }
    
    func dequeueCat() {
        self.dequeue(animal: "Cat")
    }
    
    func dequeueDog() {
        self.dequeue(animal: "Dog")
    }
    
    func dequeue(animal: String) {
        if oldest == nil {
            print("NO DATA")
            return
        }
        
        var current = self.oldest
        var prev: CNode? = nil
        if current!.next != nil {
            prev = self.oldest
        }
        
        
        while current != nil {
            if current!.data == animal {
                if current!.next == nil {
                    if prev != nil {
                        prev!.next = nil
                        print("\(animal) found")
                        return
                    } else {
                        self.oldest = nil
                        print("\(animal) found")
                        return
                    }
                    
                }
                else {
                    current!.data = current!.next!.data
                    current!.next = current!.next!.next
                    print("\(animal) found")
                    return
                }
            }
            prev = current
            current = current!.next
            
        }
        print("\(animal) not found")
    }
}

/*
var sh = CatDogList()
sh.enqueue(data:"Dog")
sh.enqueue(data:"Cat")
sh.enqueue(data:"Cat")
sh.enqueue(data:"Dog")
sh.enqueue(data:"Dog")
sh.enqueue(data:"Cat")
sh.enqueue(data:"Cat")
sh.enqueue(data:"Cat")
sh.enqueue(data:"Dog")
sh.enqueue(data:"Dog")
sh.enqueue(data:"Dog")

print(sh.dequeueAny())
print(sh.dequeueAny())

sh.dequeueCat()
sh.dequeueCat()
*/


/*
Output: 

Dog
Cat found
Cat found
Cat not found
Cat not found
Cat not found
Cat not found
Dog found
Dog found
NO DATA
NO DATA

*/
