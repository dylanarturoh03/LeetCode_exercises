from binaryHeap import MinHeap


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        '''
        Get order by using a heap for available tasks (Enqueue time focused)
        and one for ready tasks (Processing time / idx focused)
        '''
        res: list[int] = []

        for i, t in enumerate(tasks):
            t.append(i)

        deferred: list[list[int]] = MinHeap(tasks)
        ready: list[tuple[int, int]] = MinHeap()

        i: int = deferred.peek()[0]
        while deferred or ready:

            # Load valid tasks into ready
            while deferred and deferred.peek()[0] <= i:
                curr = deferred.pop()
                processingTime, idx = curr[1], curr[2]
                ready.push((processingTime, idx))

            # Process next task
            if ready:
                processingTime, idx = ready.pop()
                res.append(idx)
                i += processingTime

            # Jump to nxt task if non remain ready for processing.
            if not ready and deferred and deferred.peek()[0] > i:
                i = deferred.peek()[0]

        return res


tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
sol = Solution()
print(sol.getOrder(tasks))
