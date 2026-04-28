class Solution:
    def findMedianSortedArrays(
        self,
        nums1: list[int],
        nums2: list[int]
    ) -> float:
        def merge() -> list[int]:
            res: list[int] = []
            p1, p2 = 0, 0

            while p1 <= len(nums1) - 1 and p2 <= len(nums2) - 1:
                if nums1[p1] <= nums2[p2]:
                    res.append(nums1[p1])
                    p1 += 1
                else:
                    res.append(nums2[p2])
                    p2 += 1

            res.extend(nums1[p1:])
            res.extend(nums2[p2:])
            return res

        nums: list[int] = merge()

        if not nums:
            return float('nan')

        if len(nums) % 2 == 0:
            mid: int = len(nums) // 2
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return nums[len(nums) // 2] * 1.0

    def findMSA_logtime(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        # Algorithmic idea:
        # Partition into left and right halves
        # both arrays and adjust until a valid
        # partition is found.
        # Then get middle value or values to calculate
        # median.
        low, high = 0, len(nums1)
        n, m = len(nums1), len(nums2)

        while low <= high:
            cut1: int = (high + low) // 2
            cut2: int = (n + m) // 2 - cut1

            maxLeft: int = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            minRight: int = nums1[cut1] if cut1 < n else float('inf')
            maxLeft2: int = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            minRight2: int = nums2[cut2] if cut2 < m else float('inf')

            if maxLeft <= minRight2 and maxLeft2 <= minRight:
                if (n + m) % 2 == 0:
                    maxL: int = max(maxLeft, maxLeft2)
                    minR: int = min(minRight, minRight2)
                    return (minR + maxL) / 2
                else:
                    return min(minRight, minRight2) * 1.0
            elif maxLeft > minRight2:
                high = cut1 - 1
            else:
                low = cut1 + 1


sol = Solution()
print(sol.findMSA_logtime([1, 2], [3, 4]))
