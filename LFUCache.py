from typing import Optional


class LFUNode:
    def __init__(
        self,
        key: int = 0,
        val: int = 0,
        freq: int = 0,
        nxt: Optional['LFUNode'] = None,
        prev: Optional['LFUNode'] = None
    ):
        self.key = key
        self.val = val
        self.freq = freq
        self.nxt = nxt
        self.prev = prev


class LFUCache:
    def __init__(self, capacity: int):
        self.cap: int = capacity
        self.k: int = 0
        self.cache: dict[int, LFUNode] = {}
        self.freqs: dict[int, LFUNode] = {}
        self.dummy: LFUNode = LFUNode()

    def get(self, key: int) -> int:
        '''Get value from node with a given key.'''
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._rellocateNode(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        '''Insert of modify a node with a given key -> value pair.'''
        if key in self.cache:
            # Update node
            node = self.cache[key]
            node.val = value
            self._rellocateNode(node)
        else:
            # Manage capacity
            if self.k == self.cap:
                self._evict()
            else:
                self.k += 1

            node = LFUNode(key=key, val=value, freq=1)
            self.cache[key] = node

            # Create new node
            # Either insert after MRU of freq 1 or dummy node
            anchor = self.freqs.get(1, self.dummy)
            self._insert_after(anchor, node)
            self.freqs[1] = node

    def _insert_after(self, anchor: LFUNode, node: LFUNode) -> None:
        '''Insert a given node after a given anchor node.'''
        nxtNode = anchor.nxt
        anchor.nxt = node
        node.nxt = nxtNode
        node.prev = anchor

        if nxtNode:
            nxtNode.prev = node

    def _extract(self, node: LFUNode) -> None:
        '''Extract a given node from linked list.'''
        node.prev.nxt = node.nxt
        if node.nxt:
            node.nxt.prev = node.prev
        node.prev = node.nxt = None

    def _rellocateNode(self, node: LFUNode) -> None:
        '''
            Given a node update it's frequency by one and adjust
            position within list if needed,
        '''
        def _updateFreqs() -> None:
            '''Update MRU of node.freq if needed.'''
            if self.freqs[node.freq] == node:
                if node.prev.freq == node.freq:
                    self.freqs[node.freq] = node.prev
                else:
                    del self.freqs[node.freq]

        _updateFreqs()
        node.freq += 1

        # Rellocate given node
        if node.freq not in self.freqs:
            self.freqs[node.freq] = node

            lFNode = (
                self.freqs[node.freq - 1]
                if node.freq - 1 in self.freqs else None
            )
            # Anchor it after node's freq - 1 MRU if needed.
            if lFNode and lFNode.nxt != node:
                self._extract(node)
                self._insert_after(lFNode, node)

        else:
            # Anchor node after MRU of it's curent new freq
            lFNode = self.freqs[node.freq]
            self.freqs[node.freq] = node

            self._extract(node)
            self._insert_after(lFNode, node)

    def _evict(self) -> None:
        '''Extract head of list and evict it from all structures.'''
        # Delete LRU node within the LFU freq.
        # That node is the head / dummy.next
        evictNode = self.dummy.nxt
        self._extract(evictNode)

        del self.cache[evictNode.key]

        if self.freqs[evictNode.freq] == evictNode:
            del self.freqs[evictNode.freq]


obj = LFUCache(2)
obj.put(3, 1)
obj.put(2, 1)
obj.put(2, 2)
print(obj.get(2))
print(obj.freqs[3].key)
