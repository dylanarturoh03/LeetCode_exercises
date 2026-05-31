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
        self.freqs: dict[int, Optional[LFUNode]] = {}
        self.dummy: LFUNode = LFUNode()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._rellocateNode(node)

        return node.val

    def put(self, key: int, value: int) -> None:
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
            # Either insert after MRU of freq[1]
            if 1 not in self.freqs:
                nxtNode = self.dummy.nxt
                self.dummy.nxt = node
                node.nxt = nxtNode
                node.prev = self.dummy

                if nxtNode:
                    nxtNode.prev = node
            else:  # or after dummmy
                MRUNode = self.freqs[1]
                nxtNode = MRUNode.nxt
                MRUNode.nxt = node
                node.nxt = nxtNode
                node.prev = MRUNode

                if nxtNode:
                    nxtNode.prev = node
            self.freqs[1] = node

    def _rellocateNode(self, node: LFUNode) -> None:
        def _updateFreqs() -> None:
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

            if lFNode and lFNode.nxt != node:
                node.prev.nxt = node.nxt
                if node.nxt:
                    node.nxt.prev = node.prev
                node.prev = node.nxt = None

                lfNode_nxt = lFNode.nxt
                lFNode.nxt = node
                node.nxt = lfNode_nxt
                node.prev = lFNode

                if lfNode_nxt:
                    lfNode_nxt.prev = node

        else:
            lFNode = self.freqs[node.freq]
            self.freqs[node.freq] = node

            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            node.prev = node.nxt = None

            lfNode_nxt = lFNode.nxt
            lFNode.nxt = node
            node.nxt = lfNode_nxt
            node.prev = lFNode

            if lfNode_nxt:
                lfNode_nxt.prev = node

    def _evict(self) -> None:
        # Delete LRU node within the LFU freq.
        # That node is the head / dummy.next
        evictNode = self.dummy.nxt

        self.dummy.nxt = evictNode.nxt

        if self.dummy.nxt:
            self.dummy.nxt.prev = self.dummy
        evictNode.nxt = evictNode.prev = None

        del self.cache[evictNode.key]

        if self.freqs[evictNode.freq] == evictNode:
            del self.freqs[evictNode.freq]


obj = LFUCache(2)
obj.put(3, 1)
obj.put(2, 1)
obj.put(2, 2)
print(obj.get(2))
print(obj.freqs[3].key)
