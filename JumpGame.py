class Solution:
    def canJump(self, nums: list[int]) -> tuple[bool, list[int]]:
        goal: int = len(nums) - 1
        i: int = len(nums) - 2
        path: list[int] = [goal]

        # The idea is to chain goals from the end of the array.
        # If the last goal recorded starts
        # at index 0, then it means a valid
        # path commences there, thus, being valid
        # for the problem's requisites.

        while i >= 0:
            # This is the greedy decision
            # Invariant: Any previous goal eventually
            # leads to the end of the array.
            if i + nums[i] >= goal:
                # So, the greedy part comes in
                # declaring a position as a goal
                # the moment it connects to the curren goal.
                goal = i
                # Path is only there to showcase the greedily taken path
                path.insert(0, goal)

            i -= 1

        return goal == 0, path


sol = Solution()
print(sol.canJump([6,0,5,3,1,1,0,4,3,1,0,0]))
