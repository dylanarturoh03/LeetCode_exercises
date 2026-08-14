from binaryHeap import MaxHeap
from collections import deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        '''
        Computes minimum required cycles by simulating tasks
        using a max-heap and the cooldown using a queue.
        '''
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1

        heap = MaxHeap(list(count.values()))
        cooldown = deque([0] * n)
        cycles, empty_slots = 0, n

        while heap or empty_slots < len(cooldown):
            cycles += 1
            # Consume a task from the heap if available
            task = heap.pop() - 1 if heap else 0

            if not task:
                # Add idle cycle
                empty_slots += 1

            # Appen task to cooldown else idle cycle
            cooldown.append(task)

            # Pop elemetn at from of queue
            ready = cooldown.popleft()

            if ready:
                # If it is a task put it back in heap
                heap.push(ready)
            else:
                # Consume idle cycles
                empty_slots -= 1

        return cycles


sol = Solution()
tasks = ['A', 'A', 'A', 'B', 'C', 'B', 'B', 'C', 'C', 'D', 'E', 'F']
print(sol.leastInterval(tasks, 3))
