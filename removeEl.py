class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k: int = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return (k, nums[:k])


sol = Solution()
print(sol.removeElement([2, 3, 2, 4, 2, 2], 2))
