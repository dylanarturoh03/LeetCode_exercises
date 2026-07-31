class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        '''Get k closest by maintaining a k sized heap.'''
        heap = []
        while points:
            nxt = points.pop()
            if len(heap) < k:
                heap.append(nxt)
                self._sift_up(heap)
            elif self._get_distance(heap[0]) > self._get_distance(nxt):
                heap[0] = nxt
                self._sift_down(heap)
        return heap

    def _get_distance(self, point: list[int]) -> int:
        '''
        Compute distance squared from given point to origin in 2D space.
        '''
        x, y = point
        return x ** 2 + y ** 2

    def _sift_down(self, arr: list[list[int]], idx: int = 0) -> None:
        '''
        Bubble-down given idx value to its correct
        position based on distance squared.
        '''
        curr = lg = idx

        while True:
            lg_d = self._get_distance(arr[curr])

            left = curr * 2 + 1
            if len(arr) > left:
                left_d = self._get_distance(arr[left])
                if left_d > lg_d:
                    lg = left
                    lg_d = left_d

            right = curr * 2 + 2
            if len(arr) > right:
                right_d = self._get_distance(arr[right])
                if right_d > lg_d:
                    lg = right

            if lg == curr:
                break

            arr[lg], arr[curr] = arr[curr], arr[lg]
            curr = lg

    def _sift_up(self, arr: list[list[int]]) -> None:
        '''
        Bubble-up last element to its correct
        position based on distance squared.
        '''
        curr = len(arr) - 1

        while curr > 0:
            curr_d = self._get_distance(arr[curr])

            p = (curr - 1) // 2
            parent_d = self._get_distance(arr[p])
            if parent_d >= curr_d:
                break

            arr[curr], arr[p] = arr[p], arr[curr]
            curr = p


points = [[0, 2], [2, 8], [2, 2], [3, 1], [0, 0], [6, 2]]
# points = [[3, 2], [2, 2], [2, 8]]
sol = Solution()
print(sol.kClosest(points, 4))
