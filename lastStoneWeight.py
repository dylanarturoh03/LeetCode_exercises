class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        '''Simulate smashing the 2 heaviest rocks together using a max-heap.'''
        # Max-heapify stones
        self.max_heapify(stones)

        # While stones has more than 1 element
        while len(stones) > 1:
            # Get the two largest stones
            y = 1
            if len(stones) > 2 and stones[2] > stones[y]:
                y = 2

            diff = stones[0] - stones[y]

            stones[len(stones) - 1], stones[y] = (
                stones[y],
                stones[len(stones) - 1]
            )

            stones.pop()
            self.sift_down(stones, y)

            if diff > 0:
                # If root is bigger than second largest get rid of it,
                # then modify root's value to be the difference between
                # both stones and sift down root to it's correct pos
                stones[0] = diff
            else:
                # If they are the same replace both stones
                # with values at the end of the queue and pop them
                stones[len(stones) - 1], stones[0] = (
                    stones[0],
                    stones[len(stones) - 1]
                )

                stones.pop()

            self.sift_down(stones, 0)

        # When len of stones is less than 2 return the last stone
        # or return 0 if no stones remain.
        return stones.pop() if stones else 0

    def sift_down(self, arr: list[int], idx: int) -> None:
        largest = curr = idx
        while True:
            left = curr * 2 + 1
            if len(arr) > left and arr[largest] < arr[left]:
                largest = left

            right = curr * 2 + 2
            if len(arr) > right and arr[largest] < arr[right]:
                largest = right

            if largest == curr:
                break

            arr[curr], arr[largest] = arr[largest], arr[curr]
            curr = largest

    def max_heapify(self, arr: list[int]) -> None:
        for i in range((len(arr) - 2) // 2, -1, -1):
            self.sift_down(arr, i)


stones = [2, 2]
sol = Solution()
print(sol.lastStoneWeight(stones))
