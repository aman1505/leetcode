#1431. Kids With the Greatest Number of Candies
from typing import List

class Solution:
    def findMax(self,candies):
        max = candies[0]
        for candy in candies:
            if candy > max:
                max = candy
        return max

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = self.findMax(candies)
        result = []

        for candy in candies:
            if (candy + extraCandies) >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
        

if __name__ == '__main__':
    candies = [4,2,1,1,2]
    extraCandies = 1
    obj = Solution()
    result = obj.kidsWithCandies(candies, extraCandies)
    # result = obj.findMax(candies)
    print(result)