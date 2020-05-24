#1295. Find Numbers with Even Number of Digits
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num))%2 == 0 :
                count = count + 1
        return count
        

if __name__ == '__main__':
    nums = [12,345,2,6,7896]
    obj = Solution()
    res = obj.findNumbers(nums)
    print(res)
