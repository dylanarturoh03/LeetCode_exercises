from collections import Counter

    # Boring, yet efficient solution:
    # return Counter(s) == Counter(t)

class Solution:
    def isValidAnagram(self, s: str, t:str) -> bool:

        if len(s) != len(t):
            return False

        print(Counter(t).get('u', 0))

        for k, v in Counter(s).items():

            if (k, v) not in Counter(t).items():
                return False


        return True
    
sol = Solution()
print(sol.isValidAnagram('tar', 'rat'))