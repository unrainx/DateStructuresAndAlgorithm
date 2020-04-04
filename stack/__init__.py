
class Stack(object):
    def __init__(self, *args, **kwargs):
        self.container = []
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        return "<{}:top>".format(', '.join(self.container))

    def empty(self) -> bool:
        return self.size == 0

    def push(self, element):
        self.container.append(element)
        self.size += 1

    def top(self) -> any:
        if not self.empty():
            return self.container[-1]
        else:
            return None

    def pop(self):
        if not self.empty():
            self.container.pop(-1)
            self.size -= 1


if __name__ == "__main__":
    s = Stack()
    print(s.empty())
    s.push("111")
    s.push("111")
    s.push("111")
    s.push("111")
    s.push("111")
    s.push("111")
    s.push("111")
    s.pop()
    s.push("top")
    print("top of the stack is ", s.top())
    print(s)
