#198. House Robber
from typing import List

class Solution:    
    def rob(self, nums: List[int]) -> int:        
        sum_even = 0
        sum_odd = 0
        for i in range(len(nums)):
            if i%2 == 0:
                sum_even = sum_even + nums[i]
            else:
                sum_odd = sum_odd + nums[i]
        if sum_even > sum_odd:
            return sum_even
        else:
            return sum_odd
        
if __name__ == '__main__':
    nums = [2,7,9,3,1]
    obj = Solution()
    result = obj.rob(nums)
    print(result)

