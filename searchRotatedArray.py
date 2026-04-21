class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        # Invariant:
        # If sorted side does not contain the target, 
        # then it is present on the other side.
        while low <= high:
            mid: int = (high + low) >> 1
            if nums[mid] == target:
                return mid

            # Case: Breaking point is in right side.
            if nums[mid] >= nums[low]:

                # If target is in sorted side (left)
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:  # If target is in unsorted side (right)
                    low = mid + 1

            else:  # Case: breaking point is in left side

                # If target is in sorted side (right)
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:  # If target is in unsorted side(left)
                    high = mid - 1

        return -1


sol = Solution()
print(sol.search([1, 2, 3, 4, 5, 6], 2))
