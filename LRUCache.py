from linkedList import DoublyListNode


class LRUCache:

    def __init__(self, capacity: int):
        self.cache: dict[int, DoublyListNode] = {}
        self.cap = capacity
        self.k: int = 0
        self.dummy: DoublyListNode = DoublyListNode()
        self.tail = self.dummy

    def get(self, key: int) -> int:
        '''Return value of a node cached with a given key.'''
        if key not in self.cache:
            return -1

        self._makeNodeTail(self.cache[key])
        return self.tail.val[1]

    def put(self, key: int, value: int) -> None:
        '''Insert or modify a node with a given key:value pair.'''
        if key in self.cache:
            node = self.cache[key]
            node.val = (key, value)
            self._makeNodeTail(node)
        else:

            if self.k == self.cap:
                LUNode = self.dummy.next
                self.dummy.next = LUNode.next

                if self.dummy.next:
                    self.dummy.next.prev = self.dummy
                else:
                    self.tail = self.dummy

                LUNode.prev = LUNode.next = None

                del self.cache[LUNode.val[0]]
            else:
                self.k += 1

            newNode = DoublyListNode(val=(key, value))
            self._newTail(newNode)
            self.cache[key] = newNode

    def _newTail(self, node: DoublyListNode) -> None:
        '''Attach a given node to the tila of list.'''
        self.tail.next = node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def _makeNodeTail(self, node: DoublyListNode) -> None:
        '''Detach a given node from list and reattach it as the tail.'''
        if self.tail != node:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = node.next = None
            self._newTail(node)


obj = LRUCache(3)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
