class MyQueue:

    def __init__(self):
        self.queue = []
        self.tmp = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while self.queue:
            self.tmp.append(self.queue.pop())
        res = self.tmp.pop()
        while self.tmp:
            self.queue.append(self.tmp.pop())
        return res

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        if self.queue:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()