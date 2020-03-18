# implement of linked list
class LinkedList(object):

    class Node(object):
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self, *args, **kwargs):
        self.head = None
        self.length = 0

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
