from list import LinkedList

if __name__ == '__main__':
    link = LinkedList()
    link.add("fd")
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
