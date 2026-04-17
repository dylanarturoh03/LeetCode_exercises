class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # Algorithmic idea:
        # In order to find the pivot
        # The sum of elements to the left
        # and the sum of elements to the right
        # is needed for comparison for each element.
        prefix_sum: int = 0

        # First, a pass to compute the prefix sum is done
        # in order to know the sum of elements at i.
        for i, num in enumerate(nums):
            prefix_sum += num
            nums[i] = prefix_sum

        # A final pass is done to calculate the sums at each side per pivot.
        # Left is just the prefix before pivot.
        # Right is the last prefix sum - current prefix
        left, right = 0, 0
        for i, pivot in enumerate(nums):
            # Edge cases are when pivots are placed at the ends.
            # Since it is neccesary to handle left or right as an extension
            # of the array depending of position.
            left = 0 if i == 0 else nums[i - 1]
            right = nums[len(nums) - 1] - pivot

            if left == right:
                return i
        return -1


sol = Solution()
print(sol.pivotIndex([-1, 1]))
