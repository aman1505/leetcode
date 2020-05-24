#1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        count = 0
        for word in s:
            if len(stack) == 0:
                flag = word
                stack.append(word)
            else:                                
                if word == flag:
                    stack.append(word)
                else:
                    stack.pop()
                    if len(stack) == 0:
                        count = count + 1
        return count
        

if __name__ == "__main__":
    s = "RLRRRLLRLL"
    obj = Solution()
    result = obj.balancedStringSplit(s)
    print(result)
