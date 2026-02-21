class Solution:
    '''What I learnt:
        mod isn't just to give you the remainder of n / m,
        but also how n wraps around a cycle of size m... Plus, it is O(1).'''

    def rotate(self, nums: list[int], k: int) -> None:
        '''Rotate array to the left.'''
        aux_array: list[int] = [num for num in nums]

        for i in range(len(nums)):
            position: int = i + k

            if position > len(nums) - 1:
                loops: int = (1 if position // len(nums) == 0
                              else position // len(nums))

                for _ in range(loops):
                    position -= len(nums)

            nums[i] = aux_array[position]
        print(nums)

    def rotate_r(self, nums: list[int], k: int) -> None:
        '''Rotate array to the right'''

        aux_array: list[int] = [num for num in nums]

        for i in range(len(nums)):
            position: int = (i - k) % len(nums)

            # if position < 0:
            #    loops: int = (1 if abs(position) // len(nums) == 0
            #                  else abs(position) // len(nums))

            #    for _ in range(loops):
            #        position += len(nums)

            nums[i] = aux_array[position]
        print(nums)


sol = Solution()
sol.rotate_r([1000,2,4,-3], 3)
