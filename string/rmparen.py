class Solution:
    def removeOuterParenthese(self, s: str) -> str:
        stack = []
        result = []

        for char in s:
            if char == '(':
                if stack:
                    result.append(char)
                    stack.append(char)
                else:
                    stack.append(char)
            else:
                stack.pop()
                if stack:
                    result.append(char)

        return ''.join(result)
    

s = Solution()
print(s.removeOuterParenthese("(()())(())"))
