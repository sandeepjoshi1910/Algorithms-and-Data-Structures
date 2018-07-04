
class MaxHeap:

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self,i):
        self.heap.append(i)
        self.size = self.size + 1
        self.swapUp(self.size)
        
    def swapUp(self,i):
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i//2]
                self.heap[i//2] = tmp
            i = i // 2

    def delMax(self):
        val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size = self.size - 1
        self.swapDown(1)
        return val


    def swapDown(self,i):
        while i * 2 <= self.size:
            mc = self.maxChild(i)
            if self.heap[mc] > self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc


    def maxChild(self,i):
        if i*2 + 1 > self.size:
            return i*2
        else:
            if self.heap[i*2] > self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1


h = MaxHeap()
nums = [3,7,20,5,12,17,33,61,2]
for num in nums:
    h.insert(num)


print(h.heap)

print(h.delMax())

print(h.heap)
