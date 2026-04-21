class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Invariant:
        # The answer is always going to be a point
        # where the sorting gets broken, so the idea
        # is to search regions which are interesing, with that
        # I mean unsorted regions based on a mid/pivot and the
        # high / low pointers.

        # Sorted regions are discarded, while we look into chaotic
        # halves until our pointers cross or are equal.

        # If nums[mid] > nums[high] it means the breaking point
        # is in the upper half of nums. Otherwise, it is in the lower part.
        low, high = 0, len(nums) - 1
        while low < high:
            mid: int = (high + low) >> 1

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


sol = Solution()
print(sol.findMin([1, 2, 3, 4, 5, 6, 7]))
# [1, 2, 3, 4, 5, 6, 7]
# [7, 1, 2, 3, 4, 5, 6]
# [6, 7, 1, 2, 3, 4, 5]
# [5, 6, 7, 1, 2, 3, 4]
# [4, 5, 6, 7, 1, 2, 3]
# [3, 4, 5, 6, 7, 1, 2]
# [2, 3, 4, 5, 6, 7, 1]
