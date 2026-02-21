class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidates: dict[int, int] = {}
        res: list[int] = []
        third: int = len(nums) // 3

        for n in nums:
            candidates[n] = candidates.get(n, 0) + 1

            if len(candidates) > 2:
                new_candidates: dict[int, int] = {}
                for n in candidates:
                    candidates[n] = candidates.get(n) - 1

                    if candidates[n] != 0:
                        new_candidates[n] = candidates.get(n)

                candidates = new_candidates

        for k in candidates:
            count: int = 0

            for n in nums:
                if n == k:
                    count += 1

                    if count > third:
                        res.append(k)
                        break

        return res


sol = Solution()
print(sol.majorityElement([1, 1, 1, 1, 4, 5, 5]))
