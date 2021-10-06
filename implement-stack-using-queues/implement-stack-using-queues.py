class MyStack:

    def __init__(self):
        self.arr = []
        self.len = 0

    def push(self, x: int) -> None:
        self.len += 1
        self.arr.append(x)       
        

    def pop(self) -> int:
        self.len -= 1
        num = self.arr[self.len]
        del self.arr[self.len]
        return num
        

    def top(self) -> int:
        return self.arr[self.len - 1]
        

    def empty(self) -> bool:
        if self.len == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()