# implement of linked list
class LinkedList(object):

    class Node(object):
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self, *args, **kwargs):
        self.head = None
        self.length = 0
        self.__iter = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iter < self.length:
            i = 0
            node = self.head
            ret = None
            while i <= self.__iter:
                ret = node.element
                node = node.next
                i += 1
            self.__iter += 1
            return ret
        self.__iter = 0
        raise StopIteration

    def empty(self) -> bool:
        return self.head is None

    @staticmethod
    def last(node: Node) -> bool:
        return node.next is None

    def position(self, element) -> list:
        # 找到返回下标列表
        result = []
        position = 0
        node = self.head
        while node is not None:
            if node.element == element:
                 result.append(position)
            node = node.next
            position += 1
        return result

    def find(self, element) -> Node:
        # 最多花费O(N)
        node = self.head
        while node is not None:
            if node.element == element:
                return node
            node = node.next
        return None

    def includes(self, element) -> bool:
        return self.find(element) is not None

    def add(self, element):
        if self.head is None:
            self.head = self.Node(element)
            self.length += 1
            return

        node = self.head
        while node is not None:
            if self.last(node):
                # print("LinkedList add")
                node.next = self.Node(element)
                self.length += 1
                return
            node = node.next

    def insert(self, position: int, element):
        i = 0
        node = self.head
        while i < position:
            node = node.next
            if node is None:
                raise Exception("over in range")
            i += 1
        t = node.next
        node.next = self.Node(element)
        node.next.next = t
        self.length += 1

    def remove(self, position: int):
        i = 0
        node = self.head
        while i < position - 1:
            node = node.next
            if node is None:
                raise Exception("over in range")
            i += 1
        node.next = node.next.next
        self.length -= 1

    def retrieve(self):
        node = self.head
        while node is not None:
            print(node.element)
            node = node.next


if __name__ == '__main__':
    link = LinkedList()
    link.add("fd")
    link.add("second")
    link.add("fd")
    link.add("fd")
    link.insert(0, "0")
    print(link.length)
    link.insert(3, "0")
    link.insert(3, "0")
    link.insert(3, "0")
    link.insert(3, "0")
    link.insert(3, "0")
    link.remove(3)
    link.retrieve()
    print(link.includes("0"))
    l = LinkedList()
    # l.add(1)
    # l.add(2)
    # l.add(3)
    for i in l:
        print(i)

