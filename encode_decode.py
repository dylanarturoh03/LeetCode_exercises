class Solution:
    def enconder(self, strs: list[str]) -> str:
        print(strs)
        codedStr = ''

        for str in strs:
            for c in str:
                codedStr+= c

            codedStr+='\uFFFF'

        # return '\uFFFF'.join(strs)

        return codedStr
    
    def decoder(self, s: str) -> list[str]:
        originalList = []
        word=''

        for char in s:
            if ord(char) != 65535:
                #print(char + ' is ascii')
                word+=char
            else:
                #print('The current char isnt ascii')
                originalList.append(word)
                word=''

        #return s.split('\uFFFF')
        return originalList
    
sol = Solution()
print(sol.decoder(sol.enconder([''])))
#print(sol.decoder('Hola'))