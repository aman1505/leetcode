class Solution():
    def checkPalindrome(self,input: str)-> bool:
        transformed_input = input.replace(" ","").lower()
        for s in transformed_input:
            if (ord(s) >= 97 and ord(s) <= 122) or (ord(s) >= 48 and ord(s) <= 57):
                pass
            else:
                transformed_input=transformed_input.replace(s,"")   
        i = 0
        print(transformed_input)
        length0fString= len(transformed_input)
        flag= True
        while (i<length0fString/2):
            if transformed_input[i] == transformed_input[length0fString-1-i]:
                flag = True
            else:
                flag = False
                return flag
            i+=1
        return flag


if __name__ == "__main__":
    input = "0P"
    obj = Solution()
    result = obj.checkPalindrome(input)
    print(result)