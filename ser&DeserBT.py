from typing import Optional
from trees import TreeNode, buildBT, printBT


class codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        '''Serializes BT using preoder + # for null pointers.'''

        # Preorder is used because we can always know
        # root's position.

        # The same applies to postorder, but the traversal
        # must be done backwards.

        # None markers are added to remove the ambiguity
        # of the node's children
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                serial.append('#')
                return

            serial.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        serial = []
        dfs(root)
        return '|'.join(serial)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        '''Builds a BT from a serialized string.'''
        def dfs() -> Optional[TreeNode]:
            if tree[self.pos] == '#':
                self.pos += 1
                return None

            node = TreeNode(val=int(tree[self.pos]))
            self.pos += 1
            node.left = dfs()
            node.right = dfs()

            return node

        self.pos = 0  # Points to the lastest unconsumed token.
        tree = data.split('|')
        return dfs()


bt = buildBT([1, 2, 3, 4, 5, 6, 17])
printBT(bt)
print()

protocol = codec()
serial = protocol.serialize(bt)
print(serial)


printBT(protocol.deserialize(serial))
# bt = protocol.deserialize(serial)
# printBT(bt)
