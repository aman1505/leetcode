from typing import List
class Solution():
    def findLongestSequence(self, nums: List[int]) ->  int:
        max = nums[0]
        count=1
        for num in nums:
            if num > max:
                max = num 
            else:
                count+=1
                max = num           
        return count

if __name__ == "__main__":
    nums = [10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]
    obj = Solution()
    result = obj.findLongestSequence(nums)
    print(result)
