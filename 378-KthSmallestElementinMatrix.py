from typing import List
class Solution:
    def kthSmallest(self, nums: List[List[int]], k: int)-> int:
        result = 0
        res = []
        for num in nums:
            res+=num
        print(res)
        return result 

if __name__ == "__main__":
    nums = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    obj = Solution()
    result = obj.kthSmallest(nums,k)