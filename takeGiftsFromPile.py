from binaryHeap import MaxHeap


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        '''Use a max-heap to process and reorganize piles for k cycles.'''
        piles = MaxHeap(gifts)

        # Take and reorganize the piles
        for _ in range(k):
            curr = piles.peek()
            kept = int(curr ** 0.5)
            piles.replace(kept)

        return sum(piles)


gifts = [25, 64, 9, 4, 100]
sol = Solution()
print(sol.pickGifts(gifts, 4))
