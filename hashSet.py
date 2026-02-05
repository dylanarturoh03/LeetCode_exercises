from math import floor


class MyHashSet:
    A: float = 0.618  # Contant for hashing
    M: int = 1000  # Constant size of hash table

    def __init__(self):
        self.table: list[list[int]] = [[] for _ in range(MyHashSet.M)]

    def add(self, key: int) -> None:
        bucket: int = MyHashSet.hash_key(key)

        if self.contains(key):
            raise KeyError(f'{key} already in the set.')

        self.table[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket: int = MyHashSet.hash_key(key)

        if not self.contains(key):
            raise KeyError(f'{key} not in set.')

        self.table[bucket].remove(key)

    def contains(self, key: int) -> bool:
        bucket: int = MyHashSet.hash_key(key)
        return key in self.table[bucket]

    @staticmethod
    def hash_key(key: int) -> int:
        return floor((MyHashSet.M * (key * MyHashSet.A % 1)))


table = MyHashSet()
print(table.add(5))
print(table.contains(5))
print(table.add(5))
print(table.remove(5))
print(table.contains(5))
