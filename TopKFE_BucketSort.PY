class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        buckets = [[] for n in nums]
        topKElements = []

        for n in nums:
             count[n] = count.get(n, 0) + 1

        for n, freq in count.items():
            buckets[freq - 1].append(n) 

        for bucket in buckets[::-1]:
            topKElements.extend(bucket)
            if len(topKElements) == k:
                return topKElements

    
sol = Solution()
print(sol.topKFrequent([1, 2, 2, 3, 3], 2))