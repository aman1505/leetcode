class Solution:
    def isValid(self, strs: str) -> bool:
        stack = []
        result=True
        no_pop=False
        if len(strs)==0:
            print("inside")
            return(True)
        elif len(strs)==1 or strs[0]==')' or strs[0]==']' or strs[0]=='}':
            print("inside elif")
            return(False)
        else:
            for s in strs:
                if s in ['(','{','[']:
                    stack.append(s)
                else:
                    if len(stack)==0:
                        return(False)
                    no_pop=True
                    top = stack.pop()
                    print(top+s+"---------")
                    if top+s not in ['()','{}','[]']:
                        print("inside top+s")
                        result = False
                        break

        if result == False or no_pop==False or len(stack)>0:
                return(False)
        else:
            return(True)


if __name__ == '__main__':
    a = Solution()
    s = '()'
    print(a.isValid(s))

    # optimized
    # def isValid(self, s: str) -> bool:
    #     d = {')': '(', '}': '{', ']': '['}
    #     stack = []
    #     for i in s:
    #         if i in d.values():
    #             stack.append(i)
    #         elif not stack or stack.pop() != d[i]:
    #             return False
    #     return not stack