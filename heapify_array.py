class Solution:
    def max_heapify(self, arr: list[int]) -> list[int]:
        def sift_down(idx: int) -> None:
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

        for i in range((len(arr) - 2) // 2, -1, -1):
            sift_down(i)

        return arr

    def min_heapify(self, arr: list[int]) -> list[int]:
        def sift_down(idx: int) -> None:
            smallest = curr = idx
            while True:
                left = curr * 2 + 1
                if len(arr) > left and arr[smallest] > arr[left]:
                    smallest = left

                right = curr * 2 + 2
                if len(arr) > right and arr[smallest] > arr[right]:
                    smallest = right

                if smallest == curr:
                    break

                arr[curr], arr[smallest] = arr[smallest], arr[curr]
                curr = smallest

        for i in range((len(arr) - 2) // 2, -1, -1):
            sift_down(i)

        return arr


arr = [3, 17, 9, 42, 5, 28, 11, 1, 33]
sol = Solution()
print(sol.max_heapify(arr))
print(sol.min_heapify(arr))
