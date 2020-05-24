class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = ""
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                pair = stack.pop()+i
                if len(stack) != 0:
                    result = result + pair
                pair = ""
        return str(result)
        

if __name__ == '__main__':
    s = "(()()) (())   (()(()))"
    obj = Solution()
    result = obj.removeOuterParentheses(s)
    print(result)
