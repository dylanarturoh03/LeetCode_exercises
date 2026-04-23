class TimeMap:

    def __init__(self):
        self.timeMap: dict[str, list[str, int]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ''

        # If queried element's timestamp is greater or equal than
        # last element in the list:
        value, ts_last = self.timeMap[key][len(self.timeMap[key]) - 1]
        if ts_last <= timestamp:
            return value

        # If queried element's timestamp is smaller than
        # first element in the list:
        value, ts_first = self.timeMap[key][0]
        if timestamp < ts_first:
            return ''
        # If equal to first element:
        elif timestamp == ts_first:
            return value

        # If element is somewhere in range of list:
        low, high = 0, len(self.timeMap[key]) - 1

        while low <= high:
            mid: int = (high + low) // 2
            mid_val, mid_ts = self.timeMap[key][mid]

            if mid_ts < timestamp:
                low = mid + 1
            elif mid_ts > timestamp:
                high = mid - 1
            else:
                return mid_val
        return self.timeMap[key][high][0]

    def __str__(self):
        return f'{self.timeMap}'


obj = TimeMap()
obj.set('alice', 'happy', 1)
obj.set('alice', 'sad', 3)
obj.set('alice', 'excited', 5)
obj.set('alice', 'confused', 7)
obj.set('arthur', 'hopeful', 4)
print(obj)
print(obj.get('alice', 99))
