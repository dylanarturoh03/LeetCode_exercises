class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        # Invariant:
        # The array has a sorted and potentially unsorted side.
        # Since the sorted side is predictable we must identify it
        # and determine the side where the target could be based on it's
        # membership to the sorted half.

        # Pretty much the same problem as search in sorted array I, but
        # with the addition of duplicates you can have cases where all 3
        # key nums are the same, which would leave us without enough
        # information to move forward.

        # Why? Because the sorted part could be anywhere...
        # Example:
        # nums[low] == nums[mid] == nums[high] == 2

        # 2, 2, 2, 2, 2, 2, 2
        # 2, 0, 1, 2, 2, 2, 2
        # 2, 2, 2, 2, 0, 1, 2

        # As you can see here they are all possible when having only 2's
        # and there is no way to know currently, so we shrink in hopes of
        # finding more meaningful candidates.

        # This shrinking behavior causes the worst case complexity
        # to increase to O(N) time, because we could end up shrinking the
        # entire or most of the array, which would be O(1/2N) so just linear.
        while low <= high:
            mid: int = (high + low) // 2

            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] == nums[high]:
                # Shrinking behavior
                low += 1
                high -= 1
                continue

            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False


sol = Solution()
print(sol.search([3, 5, 6, 0, 0, 1, 2], 3))
