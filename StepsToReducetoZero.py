class Solution:
    def isEven(self,num):
        if(num%2==0):
            return True
        return False
    
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while (num!=0):
            if self.isEven(num):
                num = num/2
            else:
                num = num -1
            count = count + 1 
        return count


if __name__ == '__main__':
    num = 123
    obj = Solution()    
    res = obj.numberOfSteps(num)
    print(res)