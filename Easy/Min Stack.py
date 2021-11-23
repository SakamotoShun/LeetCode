class MinStack:

    def __init__(self):
        self.Arr = []

    def push(self, val: int) -> None:
        if not self.Arr:
            self.Arr.append([val, val])
            return
        Minimum = self.Arr[-1][1]
        Add = min(val, Minimum)
        self.Arr.append([val, Add])

    def pop(self) -> None:
        self.Arr.pop()

    def top(self) -> int:
        return self.Arr[-1][0]

    def getMin(self) -> int:
        return self.Arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()