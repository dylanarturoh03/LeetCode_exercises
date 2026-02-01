class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]] :

        anagramList = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in anagramList:
                anagramList[sortedWord].append(word)
            else:
                anagramList[sortedWord] = [word]


        return list(anagramList.values())
    
sol = Solution()
print(sol.groupAnagrams([""]))