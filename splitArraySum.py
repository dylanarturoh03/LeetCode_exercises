class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        '''Binary search on answer:
        split array into k parts minimizing max part sum'''

        # Define search space
        # low = min sum to form n partitions
        # high = Exact sum to form 1 partition
        lo, hi = max(nums), sum(nums)
        minLSAS: int = hi
        # Idea:
        # Do binary search on the answer space (in this case the
        # maxArraySums) and find the smallest one that can split
        # the array in less than or equal to k partitions.
        while lo <= hi:
            maxSum: int = (hi + lo) // 2
            n_partitions, prefix_sum = 1, 0
            for n in nums:
                # In order to know the min number of splits with
                # a maxSum constraint we lazily form partitions as
                # is requiered in order to not surpass maxSum.
                if prefix_sum + n > maxSum:
                    n_partitions += 1
                    prefix_sum = 0
                prefix_sum += n

            # If we can partition the array in less or equal pieces than K
            # it means we could maybe still find a smaller maxSum that satisfy
            # the k_partitions constraint.
            if n_partitions <= k:
                minLSAS = maxSum
                hi = maxSum - 1
            else:
                # If not, then we eliminate all the smaller maxSums
                # by shrinking the search space to the left.
                lo = maxSum + 1

        return minLSAS


sol = Solution()
print(sol.splitArray([8, 7, 4, 1, 5, 0, 3, 7], 2))
