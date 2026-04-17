class Solution:
    def jump(self, nums: list[int]) -> int | float:
        if not nums:
            return float('inf')
        if len(nums) == 1:
            return 0
        # Algorithmic idea:
        # From index i, we can reach all positions in (i + 1, i + nums[i])
        # in one jump.
        # Among those positions we look for the index j that will get us the
        # longest j + nums[j] (longest future reach)
        i: int = 0
        j: int = 0
        k: list[int, int] = [0, 0]
        jumps: int = 0

        while i + nums[i] < len(nums) - 1:
            j = i + nums[i]

            k[0], k[1] = j, nums[j]

            j -= 1

            while j > i:
                # Greedy decision:
                # At each local window we track inside k
                # [j, nums[j]] that will give us
                # the maximum future reach.
                if nums[j] + j > k[0] + k[1]:
                    k[0], k[1] = j, nums[j]

                j -= 1

            # The we move (or 'jump') to optimal j.
            jumps += 1
            i = k[0]

        return jumps + 1


sol = Solution()
print(sol.jump([2, 5, 1, 1, 1, 0]))
