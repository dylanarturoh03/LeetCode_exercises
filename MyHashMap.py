from math import floor


class MyHashMap:
    A: float = 0.618
    M: int = 20_011
    TOMBSTONE: object = object()
    EMPTY: None = None

    def __init__(self):
        self.table = [[MyHashMap.EMPTY] for _ in range(MyHashMap.M)]

    def put(self, key: int, value: int) -> None:
        bucket: int = MyHashMap.hash_key(key)

        while True:
            position = self.table[bucket][0]

            if position == key:
                self.table[bucket][1] = value
                break
                # raise KeyError(f'{key} already exists.')

            if (position is MyHashMap.EMPTY or
                    position is MyHashMap.TOMBSTONE):
                self.table[bucket] = [key, value]
                break

            bucket = (bucket + 1) % MyHashMap.M

    def get(self, key: int) -> int:
        bucket: int = MyHashMap.hash_key(key)

        while True:
            position = self.table[bucket][0]

            if position is MyHashMap.EMPTY:
                # return -1
                raise KeyError(f'{key} does not exist.')

            if position is MyHashMap.TOMBSTONE:
                bucket = (bucket + 1) % MyHashMap.M
                continue

            if position == key:
                return self.table[bucket][1]

            bucket = (bucket + 1) % MyHashMap.M

    def remove(self, key: int) -> None:
        bucket: int = MyHashMap.hash_key(key)

        while True:
            position = self.table[bucket][0]

            if position is MyHashMap.EMPTY:
                # break
                raise KeyError(f'{key} does not exist.')

            if position is MyHashMap.TOMBSTONE:
                bucket = (bucket + 1) % MyHashMap.M
                continue

            if position == key:
                self.table[bucket] = [MyHashMap.TOMBSTONE]
                break

            bucket = (bucket + 1) % MyHashMap.M

    @staticmethod
    def hash_key(key: int) -> int:
        return floor((MyHashMap.M * (key * MyHashMap.A % 1)))


hashmap = MyHashMap()
hashmap.put(3, 8)
hashmap.put(8, 8)
hashmap.put(3, 5)
print(hashmap.table)
