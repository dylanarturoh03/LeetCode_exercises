class Solution:
    def bubble_sort(self, nums: list[int]) -> list[int]:
        bubble: int = len(nums)
        swap: bool = False

        for _ in range(len(nums)):
            for j in range(bubble - 1):
                current: int = nums[j]
                next_element: int = nums[j + 1]

                if current > next_element:
                    nums[j], nums[j + 1] = next_element, current
                    swap = True

            if not swap:
                break

            bubble -= 1

        return nums


sol = Solution()
print(sol.bubble_sort([1, 5, 2, 4, 17, 1, 3]))
