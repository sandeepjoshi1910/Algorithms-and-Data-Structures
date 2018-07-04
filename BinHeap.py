
class BinHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self,item):
        self.heapList.append(item)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc


    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        val = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return val


h = BinHeap()
nums = [10,5,7,2,22,56,78,23,33,12,2,90,1]
for num in nums:
    h.insert(num)

for i in range(0,8):
    print(h.delMin())