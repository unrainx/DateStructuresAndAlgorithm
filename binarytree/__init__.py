

# implement of binary search tree
#           6
#         /  \
#       2     8
#     /  \
#   1     4
class BinaryTree(object):

    class Node(object):
        def __init__(self, element, left=None, right=None):
            self.element: int = element
            self.count: int = 1
            self.left: BinaryTree.Node = left
            self.right: BinaryTree.Node = right

    def __init__(self):
        self.root: BinaryTree.Node = None

    def empty(self) -> bool:
        return self.root is None

    def insert(self, element: int):

        def _insert(n: BinaryTree.Node) -> BinaryTree.Node:
            if n is None:
                n = BinaryTree.Node(element)
            elif element < n.element:
                n.left = _insert(n.left)
            elif element > n.element:
                n.right = _insert(n.right)
            return n

        node = self.find(element)
        if node is not None:
            node.count += 1
        else:
            node = self.root
            self.root = _insert(node)

    def delete(self, element: int):
        node = self.find(element)
        if node is not None:
            node.count -= 1

    def find(self, element) -> Node:
        if self.empty():
            return None

        def _find(n: BinaryTree.Node) -> BinaryTree.Node:
            if n is None:
                return None
            if element < n.element:
                return _find(n.left)
            elif element > n.element:
                return _find(n.right)
            else:
                if n.count <= 0:
                    return None
                return n

        node = self.root
        return _find(node)

    def min(self) -> Node:
        if self.empty():
            return None
        node = self.root
        while node.left is not None:
            node = node.left
        return node

    def max(self) -> Node:
        if self.empty():
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node

    def print_tree(self):
        if self.empty():
            print("this node is empty.")

        def print_node(n: BinaryTree.Node):
            if n is None:
                return
            if n.count > 0:
                print(n.element)
            print_node(n.left)
            print_node(n.right)

        node = self.root
        print_node(node)


if __name__ == "__main__":
    st = BinaryTree()
    st.root = BinaryTree.Node(6, BinaryTree.Node(2, BinaryTree.Node(1), BinaryTree.Node(4)), BinaryTree.Node(8))
    st.insert(10)
    st.print_tree()
    print(st.find(1).element)
    print(st.min().element)
    print(st.max().element)

    print("*** other tree ***")
    st2 = BinaryTree()
    for e in [6, 2, 4, 1, 8, 10]:
        st2.insert(e)

    st2.delete(10)
    st2.delete(2)
    print(st2.max().element)
    st2.print_tree()

