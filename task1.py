class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        print('[', end='')
        while current:
            print(current.data, end=', ')
            current = current.next
        print(']')

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next, cur.next = cur.next, prev
            prev, cur = cur, next
        self.head = prev

    def sort(self):
        _sorted = LinkedList()

        def insert(node):
            if not _sorted.head or _sorted.head.data >= node.data:
                _sorted.insert_at_beginning(node.data)
                return

            _cur = _sorted.head

            while _cur.next:
                if _cur.next.data >= node.data:
                    _sorted.insert_after(_cur, node.data)
                    return

                _cur = _cur.next

            _sorted.insert_at_end(node.data)

        cur = self.head

        while cur:
            insert(cur)
            cur = cur.next

        self.head = _sorted.head

    def merge(self, other):
        cur = other.head

        while cur:
            self.insert_at_end(cur.data)
            cur = cur.next
        self.sort()


lst1 = LinkedList()

lst1.insert_at_end(5)
lst1.insert_at_end(4)
lst1.insert_at_end(8)
lst1.insert_at_end(8)
lst1.insert_at_end(1)
lst1.insert_at_end(10)

lst1.print_list()
# [5, 4, 8, 8, 1, 10, ]

lst1.reverse()
lst1.print_list()
# [10, 1, 8, 8, 4, 5, ]

lst1.sort()
lst1.print_list()
# [1, 4, 5, 8, 8, 10, ]

lst2 = LinkedList()
[lst2.insert_at_end(i) for i in range(1, 21, 2)]

lst2.print_list()
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, ]

lst1.merge(lst2)
lst1.print_list()
# [1, 1, 3, 4, 5, 5, 7, 8, 8, 9, 10, 11, 13, 15, 17, 19, ]
