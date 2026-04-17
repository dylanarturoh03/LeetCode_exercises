class Solution:
    def simplifyPath(self, path: str) -> str:
        stack: list[str] = []
        l: int = 0
        # Invariant:
        # Stack contains only valid directories.
        while l < len(path):
            match path[l]:
                case '/':
                    while l < len(path) and path[l] == '/':
                        l += 1

                case '.':
                    seq: list[str] = []
                    hasChars: bool = False
                    while l < len(path) and path[l] != '/':
                        if not hasChars and path[l] != '.':
                            hasChars = True
                        seq.append(path[l])
                        l += 1

                    if hasChars or len(seq) > 2: 
                        stack.append(''.join(seq))
                    elif len(seq) == 2:
                        if stack:
                            stack.pop()

                case _:
                    seq: list[str] = []
                    while l < len(path) and path[l] != '/':
                        seq.append(path[l])
                        l += 1
                    stack.append(''.join(seq))

        return '/' + '/'.join(stack)


sol = Solution()
print(sol.simplifyPath("..h"))
