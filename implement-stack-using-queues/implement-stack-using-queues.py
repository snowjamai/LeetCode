from collections import deque

class MyStack:

    def __init__(self):
        self.Q = deque()

    def push(self, x: int) -> None:
        self.Q.append(x)
        

    def pop(self) -> int:
        return self.Q.pop()
        

    def top(self) -> int:
        return self.Q[-1]       

    def empty(self) -> bool:
        if len(self.Q) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()