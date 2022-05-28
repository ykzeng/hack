class Node:
    def __init__(self, k, val, prev=None, nex=None):
        self.k = k
        self.val = val
        self.prev = prev
        self.next = nex


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}
        self.capacity = capacity

    def _remove(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev

    def _add(self, node):
        tail = self.tail.prev
        tail.next = node

        node.prev = tail
        node.next = self.tail

        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self._remove(node)
        node = Node(key, value)
        self._add(node)
        self.d[key] = node
        if self.capacity < len(self.d):
            head = self.head.next
            self._remove(head)
            del self.d[head.k]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
