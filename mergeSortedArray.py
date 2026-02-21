class Solution:
    def merge(self, nums1: list[int], m: int,
              nums2: list[int], n: int) -> None:

        p1: int = 0
        p2: int = 0

        while p2 < n and p1 < m + n:
            # Error: Assuming every 0 past the fixed boundary m is placeholder.
            # After insertions, the valid sorted region grows.
            # Correct boundary is m + p2
            # (original valid elements + inserted elements).
            # Use this dynamic boundary to determine where insertion is safe.
            if nums2[p2] < nums1[p1] or p1 >= m + p2:
                aux: int = nums1[p1]
                nums1[p1] = nums2[p2]

                for i in range(p1 + 1, n + m):
                    nums1[i], aux = aux, nums1[i]

                p2 += 1

            p1 += 1
        print(nums1)


sol = Solution()
print(sol.merge([-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 5,
                [-1, -1, 0, 0, 1, 2], 6))
