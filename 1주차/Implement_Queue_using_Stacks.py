class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:

        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        # 순서가 뒤집혀있으니까 다시 넣어줘야함.
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        # print("s1: ", self.s1)
        # print("s2: ", self.s2)

    def pop(self) -> int:
        ret = self.s1.pop()

        return ret

    def peek(self) -> int:
        ret = self.s1.pop()
        self.s1.append(ret)
        return ret

    def empty(self) -> bool:
        return len(self.s1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()