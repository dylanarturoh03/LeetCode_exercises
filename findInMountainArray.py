from abc import ABC, abstractmethod


class MountainArray(ABC):
    @abstractmethod
    def get(self, index: int) -> int:
        pass

    @abstractmethod
    def length(self) -> int:
        pass


class MountainArrayImpl(MountainArray):
    def __init__(self, arr: list[int]):
        self._arr = arr

    def get(self, index: int) -> int:
        return self._arr[index]

    def length(self) -> int:
        return len(self._arr)


class Solution:
    def findInMountainArray(
        self,
        target: int,
        mountainArr: 'MountainArray'
    ) -> int:
        # Algorithmic idea:
        # A mountain array is one which has a single peak value somewhere in
        # the middle, the left side is always monotonically increasing
        # and right side is monotonically decreasing. They converge at peak.

        # NO DUPLICATES CAN BE PRESENT WITHIN A SIDE.

        # This insight about the general structure of the array is key
        # for designing an efficient solution...

        # First, the peak must be determined
        # Look for peak
        length: int = mountainArr.length()
        lo, hi = 1, length - 2
        while True:
            # Peak is the biggest integer in the array.
            mid: int = (hi + lo) // 2
            mid_val = mountainArr.get(mid)
            # If candidate is smaller than element
            # to the left:
            if mid_val < mountainArr.get(mid - 1):
                # We look leftward
                hi = mid - 1
            elif mid_val < mountainArr.get(mid + 1):
                # If candidate is smaller than element
                # to the right:
                # We look rightward.
                lo = mid + 1
            else:
                # When we find an element that is bigger
                # than both adjacent elements it means
                # the peak has been found.
                if target == mid_val:
                    # Early exit in case target == peak
                    return mid
                peak_pos, peak_val = mid, mid_val
                break
        # Now that we know the peak, the left and right sides
        # can be easily determined.

        # Due to the monotonicity of each side, we can determine
        # if a side is worth searching in by just checking
        # if value could be in range of each side.

        # If target could be in range of arr[0] to peak:
        # Search left side.
        # Left is tried first, because we are looking for
        # the first occurence of target.
        if mountainArr.get(0) <= target < peak_val:
            lo, hi = 0, peak_pos - 1

            while lo <= hi:
                mid = (hi + lo) // 2
                mid_val = mountainArr.get(mid)
                if mid_val < target:
                    lo = mid + 1
                elif mid_val > target:
                    hi = mid - 1
                else:
                    # Early exit if target is found in left side.
                    return mid

        # If left side didn't contain target, we do the same process
        # for right side.
        # If target could be in range of peak to end of mountainArr:
        if peak_val > target >= mountainArr.get(length - 1):
            lo, hi = peak_pos + 1, length - 1

            while lo <= hi:
                mid = (hi + lo) // 2
                mid_val = mountainArr.get(mid)
                if mid_val < target:
                    hi = mid - 1
                elif mid_val > target:
                    lo = mid + 1
                else:
                    return mid
        # If neither side could contain it, then it means
        # the target doesn't exist within mountainArr.
        return -1


arr: 'MountainArray' = MountainArrayImpl(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, -2]
)
sol = Solution()
print(sol.findInMountainArray(10, arr))
