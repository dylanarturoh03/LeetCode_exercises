class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority: int = len(nums) // 2
        seenElements: dict[int, int] = {}

        for i in nums:
            seenElements[i] = seenElements.get(i, 0) + 1
            if seenElements[i] > majority:
                return i


sol = Solution()
print(sol.majorityElement([5, 5, 1, 1, 1, 5, 5, 6, 5]))
