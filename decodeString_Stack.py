class Solution:
    def decodeString(self, s: str) -> str:
        block_stack: list[list[str]] = []
        k_stack: list[int] = []
        curr: list[str] = []
        l: int = 0

        while l < len(s):
            match s[l]:
                case str() if s[l].isdigit():
                    n_seq: list[str] = []
                    while l < len(s) and (s[l].isdigit() or s[l] == '|'):
                        if s[l] == '|':
                            curr.extend(n_seq)
                            n_seq = []
                            l += 1
                            continue
                        n_seq.append(s[l])
                        l += 1

                    if l == len(s) or s[l] != '[':
                        curr.extend(n_seq)
                    else:
                        if not n_seq:
                            n_seq.append('0')
                        k_stack.append(int(''.join(n_seq)))

                case '[':
                    if l == 0 or not (s[l - 1].isdigit() or s[l - 1] == '|'):
                        k_stack.append(0)
                    block_stack.append(curr)
                    curr = []
                    l += 1

                case ']':
                    prev: list[str] = block_stack.pop()
                    prev.extend(curr * k_stack.pop())
                    curr = prev
                    l += 1

                case _:
                    curr.append(s[l])
                    l += 1

        return ''.join(curr)


sol = Solution()
print(sol.decodeString('a200|1|2|3[b2[e]]'))
