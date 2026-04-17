class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        # Invariant:
        # At each step we halve the pool of candidates
        # depending of how nums[mid] compares to the target
        while low <= high:
            mid: int = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        # If low surpasses high it means the element
        # is not present in the array.
        return -1

    def search_recursive(self, nums: list[int], target: int) -> int:
        def halve(low: int, high: int) -> int:
            if low > high:
                return -1
            else:
                mid: int = (high + low) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    return mid
                return halve(low, high)

        return halve(0, len(nums) - 1)


sol = Solution()
print(sol.search([-1, 0, 2, 4, 6, 8], 3))
