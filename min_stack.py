class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ds = []

    def push(self, val: int) -> None:
        self.ds.append(val)

    def pop(self) -> None:
        if len(self.ds) != 0:
            self.ds.pop()

    def top(self) -> int:
        if len(self.ds) != 0:
            return self.ds[-1]

    def get_min(self) -> int:
        if len(self.ds) != 0:
            my_min = self.ds[0]
            for num in self.ds:
                if num < my_min:
                    my_min = num
            return my_min


if __name__ == '__main__':
    my_stack = MinStack()
    print(my_stack.top(), end=', ')
    print(my_stack.get_min(), end=', ')
    my_stack.pop()
    my_stack.push(-1)
    my_stack.push(3)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top(), end=', ')
    my_stack.pop()
    my_stack.push(-2)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top())
