class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        rescue_boats: int = 0
        l: int = 0
        r: int = len(people) - 1
        people.sort()

        if len(people) == 1:
            return 1

        while l < r:
            people_weight: int = people[l] + people[r]

            if people_weight <= limit:
                l += 1

            r -= 1

            if l == r:
                rescue_boats += 2
            else:
                rescue_boats += 1

        return rescue_boats


sol = Solution()
print(sol.numRescueBoats([1, 2, 3, 4, 5], 5))
