class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.stack = collections.deque([])

    def next(self, val: int) -> float:
        if self.size > len(self.stack):
            self.stack.append(val)
        else:
            self.stack.popleft()
            self.stack.append(val)
        return sum(self.stack) / len(self.stack)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
