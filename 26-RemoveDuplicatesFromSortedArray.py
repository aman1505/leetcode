from typing import  List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int :
        count=0
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                nums[i+1] = nums[i+2] 
                count = count+1
        return count+1


if __name__ == "__main__":
    nums = [1,1,2]
    obj = Solution()
    result = obj.removeDuplicates(nums)
    print(result)
