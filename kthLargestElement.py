from binaryHeap import MinHeap


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        '''
        Find kth largest by maintaining a
        min-heap of the k largest elements in nums.
        '''
        heap = MinHeap()

        for n in nums:
            if len(heap) < k:
                heap.push(n)
            elif heap.peek() < n:
                heap.replace(n)

        return heap.peek()


nums = [2, 3, 1, 1, 5, 5, 4]
sol = Solution()
print(sol.findKthLargest(nums, 3))
