class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        '''Preprocess nums by ordering to make kth computation constant'''
        nums.sort()
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        '''Add val to nums while maintaning ordering. Copmute and return kth'''
        if not self.nums or val >= self.nums[-1]:
            self.nums.append(val)

        else:
            for i, n in enumerate(self.nums):
                if n >= val:
                    self.nums.insert(i, val)
                    break

        return self.nums[len(self.nums) - self.k]


obj = KthLargest(1, [6])
print(obj.add(3))
print(obj.add(5))
print(obj.add(6))
print(obj.add(7))
print(obj.add(8))
