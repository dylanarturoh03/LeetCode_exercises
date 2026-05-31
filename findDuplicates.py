class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0

        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]

        return nums[fast]


sol = Solution()
print(sol.findDuplicate([1, 2, 3, 4, 2]))
