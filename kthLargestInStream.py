class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        '''Preprocess nums to create a k size min-heap.'''
        self.k = k
        self.nums = self._min_heapify(nums)
        for _ in range(len(self.nums) - k):
            self._pop()

    def add(self, val: int) -> int:
        '''
        Determine if val goes in heap,
        then move it to correct pos if needed.
        '''
        if self.k > len(self.nums):
            self.nums.append(val)
            self._sift_up()
        elif self.nums[0] < val:
            self.nums[0] = val
            self._sift_down(self.nums)

        return self.nums[0]

    def _sift_down(self, arr: list[int], idx: int = 0) -> None:
        '''Bubble-down given idx value to it's correct position.'''
        curr = mn = idx

        while True:
            left = curr * 2 + 1
            if len(arr) > left and arr[left] < arr[mn]:
                mn = left

            right = curr * 2 + 2
            if len(arr) > right and arr[right] < arr[mn]:
                mn = right

            if mn == curr:
                break

            arr[mn], arr[curr] = arr[curr], arr[mn]
            curr = mn

    def _sift_up(self) -> None:
        '''Bubble-up last element to it's correct position.'''
        curr = len(self.nums) - 1

        while curr > 0:
            p = (curr - 1) // 2
            if self.nums[p] <= self.nums[curr]:
                break

            self.nums[curr], self.nums[p] = self.nums[p], self.nums[curr]
            curr = p

    def _pop(self) -> int:
        '''Pop root from min-heap.'''
        self.nums[-1], self.nums[0] = self.nums[0], self.nums[-1]
        removed = self.nums.pop()
        self._sift_down(self.nums)

        return removed

    def _min_heapify(self, arr: list[int]) -> list[int]:
        '''Enforce min-heap conditions to a given array.'''
        for i in range((len(arr) - 2) // 2, -1, -1):
            self._sift_down(arr, i)

        return arr


obj = KthLargest(3, [1, 2, 3, 4])
print(obj.add(0))
print(obj.nums)
print(obj.add(5))
print(obj.add(6))
print(obj.add(7))
print(obj.add(8))
print(obj.nums)
