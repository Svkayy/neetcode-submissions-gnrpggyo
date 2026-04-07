from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()
        self.tmp = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.tmp.append(self.queue.popleft())
        res = self.queue.popleft()
        while self.tmp:
            self.queue.append(self.tmp.popleft())
        return res
        

    def top(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()