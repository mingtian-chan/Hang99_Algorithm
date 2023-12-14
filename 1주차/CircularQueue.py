class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.cnt = 0
        self.headidx = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[(self.headidx + self.cnt) % self.size] = value
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.headidx = (self.headidx + 1) % self.size
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.headidx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.headidx + self.cnt - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()