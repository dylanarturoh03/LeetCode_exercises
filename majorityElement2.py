class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        me: set[int] = set()
        count: dict[int, int] = {}
        third: int = len(nums) // 3

        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > third and n not in me:
                me.add(n)

            if len(me) == 2:
                break

        return list(me)


sol = Solution()
print(sol.majorityElement([5, 2, 3, 2, 2, 2, 2, 5, 5, 5]))
