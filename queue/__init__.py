
class Queue(object):
    # 循环队列实现
    # 双端队列需要实现 inject eject push pop 四种操作, 队列头和尾部都可以进行插入和删除操作
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.container = [None] * capacity
        self.size = 0
        self.front = 1
        self.rear = 0

    def __len__(self):
        return self.size

    def empty(self) -> bool:
        # 有些实现用 rear == front - 1 表示空队列
        return self.size == 0

    def full(self) -> bool:
        return self.size == self.max_capacity

    def __incre_index(self, ptr):
        return (ptr + 1) % self.max_capacity

    def __decre_index(self, ptr):
        index = ptr - 1
        if index == -1:
            index = self.max_capacity - 1
        return index

    def enqueue(self, element):
        if self.full():
            raise IndexError
        else:
            self.size += 1
            self.rear = self.__incre_index(self.rear)
            self.container[self.rear] = element

    def dequeue(self):
        if not self.empty():
            ret_index = self.front
            self.front = self.__incre_index(self.front)
            self.size -= 1
            return self.container[ret_index]
        else:
            raise IndexError


if __name__ == "__main__":
    q = Queue(10)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print("front", q.front)
    print("rear", q.rear)
    for i in range(0, len(q)):
        print(q.dequeue())
    print("front", q.front)
    print("rear", q.rear)
    print(q.empty())