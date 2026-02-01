class Solution:
    def replaceElement(self, arr: list[int]) -> list[int]:
        maxRight = -1  # arr[len(arr) - 1]

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]

            # if i == len(arr) - 1:
            #    arr[i] = -1
            # else:
            #    arr[i] = maxRight

            arr[i] = maxRight

            # if aux > maxRight:
            #    maxRight = aux

            maxRight = max(maxRight, current)

        return arr


sol = Solution()
print(sol.replaceElement([2, 4, 5, 3, 1, 2]))
