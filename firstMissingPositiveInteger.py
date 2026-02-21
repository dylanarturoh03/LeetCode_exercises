class Solution:
    # First solution I came up with
    # Time complexity: O(n log n)
    # Space complexity: O(1)
    def firstMissingPositive(self, nums: list[int]) -> int:
        first_positive: int = 1
        nums.sort()
        nums.insert(0, 0)

        for i in range(1, len(nums)):
            if nums[i] <= 0 or nums[i - 1] == nums[i]:
                continue

            if nums[i] != first_positive:
                return first_positive

            first_positive += 1

        return first_positive

    # Second solution I came up with
    # Time complexity: O(n)
    # Space complexity: O(n)
    def firstMissingPositive_LinearTimeSpace(self, nums: list[int]) -> int:
        '''
        Docstring for firstMissingPositive_LinearTimeSpace

        Method to find the first missing positive integer
        in an array of integers.

        :param self: Current instance.
        :param nums: List of numbers.
        :type nums: list[int]
        :return: First missing positive in the array.
        :rtype: int
        '''
        first_positive: int = 1
        set_nums: set[int] = {num for num in nums if num > 0}

        for _ in range(len(set_nums)):
            if first_positive not in set_nums:
                return first_positive

            first_positive += 1

        return first_positive


sol = Solution()
help(sol.firstMissingPositive_LinearTimeSpace)
print(sol.firstMissingPositive_LinearTimeSpace([1, 5, 7, 2, 3, 6, -9, -188]))
