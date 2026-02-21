class Solution:
    def subarraysum(self, nums: list[int], k: int) -> int:
        seen: dict[int, int] = {0: 1}
        prefix_sum: int = 0
        valid_subarrays: int = 0

        for j in nums:
            prefix_sum += j
            needed: int = prefix_sum - k

            if needed in seen:
                valid_subarrays += seen[needed]

            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return valid_subarrays


sol = Solution()
print(sol.subarraysum([1, -1, 1, -1, 5], 0))
