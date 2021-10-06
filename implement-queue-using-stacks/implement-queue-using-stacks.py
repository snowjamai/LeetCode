class MyQueue:

    def __init__(self):
        self.S = []
        

    def push(self, x: int) -> None:
        self.S.append(x)

    def pop(self) -> int:
        if len(self.S) != 0:
            num = self.S[0]
            del self.S[0]
            return num
        return null

    def peek(self) -> int:
        return self.S[0]
        

    def empty(self) -> bool:
        if len(self.S) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()