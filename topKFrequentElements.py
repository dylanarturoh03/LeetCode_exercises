class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        popularity = {} # Hashmap to store popularity per element (Element : Count)
        topkElements = [] # List that contains the top K elements

        # Count the popularity of each element
        for i in nums:

            if i in popularity:
                popularity[i] += 1
            else:
                popularity[i] = 1
        
        # Sort and slice the K element's popularity in a descending order
        popularityOrder = sorted(list(popularity.values()), reverse=True)[:k]

        # Store the elements whose popularity matches the values present in top popularity list
        for i in popularity.keys():

            if popularity[i] in popularityOrder:
                topkElements.append(i)
            


        return topkElements
    
sol = Solution()
print(sol.topKFrequent([1, 2, 3, 7, 3, 4, 2, 8], ))