from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        sum=0
        for num in nums:
            sum=sum+num
            result.append(sum)
        return result


if __name__ == "__main__":
    input= [3,1,2,10,1]
    obj = Solution()
    result = obj.runningSum(input)
    print(result)




