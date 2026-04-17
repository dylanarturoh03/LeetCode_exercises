class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        candidates: set[int] = set()
        for i in range(len(gas)):
            start: int = gas[i] - cost[i]
            if start > 0:
                candidates.add(i)

        for c in candidates:
            curr_gas: int = 0
            for j in range(c, len(gas) + c):
                curr_index: int = j % len(gas)
                curr_gas += gas[curr_index] - cost[curr_index]
                if curr_gas < 0:
                    break
            if curr_gas >= 0:
                return c

        return -1

    def canCompleteCircuit_Greedy(self, gas: list[int], cost: list[int]) -> int:
        # Algorithmic idea:
        # We do a one pass evaluating segments starting at current_index
        # then we evaluate that segment until it can't reach the next station
        # or it reaches the end of the circuit.
        # The core idea is that if a segment starting from s can't reach f
        # then every index between s and f is invalid as a starting point,
        # so we evaluate f + 1 as our next start.
        full_gas: int = 0
        current_start: int = 0
        current_tank: int = 0

        for i in range(len(gas)):
            # Greedy decision:
            # We ditch a segment starting from current_start
            # the moment it can't reach current station.
            # Also, in this problem we are guaranteed only one answer.
            # So, we don't need to worry about
            # more then than one valid start.
            current_tank += gas[i] - cost[i]
            full_gas += gas[i] - cost[i]
            if current_tank < 0:
                current_tank = 0
                current_start = i + 1
            # In the return we just make sure it is actually solvable.
        return current_start if full_gas >= 0 else -1


sol = Solution()
print(sol.canCompleteCircuit_Greedy([1, 2, 3, 4], [2, 2, 4, 1]))
