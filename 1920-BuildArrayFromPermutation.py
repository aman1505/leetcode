from typing import List
class Solution:
    def buildArray(self, nums: List[int])-> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result

if __name__ == "__main__":
    nums = [0,2,1,5,3,4]
    obj = Solution()
    result = obj.buildArray(nums)
    print(result)