from typing import List

class Solution:
    def findDuplicate(self, nums: List[int])-> int:
        result = -1
        count =0 
        for i in range(len(nums)):
            count = 0 
            for j in range(len(nums)):                
                if nums[i]==nums[j]:
                    count+=1
                    result = nums[i]
                    if count > 1:
                        return result 
        return result
    
    def findDuplicate2(self, nums: List[int]) -> int:
        count = [0] * (len(nums)+1)
        print(count)
        for val in nums:
            count[val] = count[val] + 1
        print(count)
        for i in range(len(count)):
            if count[i] > 1:
                return i
    
    def findDuplicate3(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num in map.keys():
                return num
            else:
                map[num] = 1
        return -1

if __name__ == "__main__":
    nums = [313,112,313,4,2]
    obj = Solution()
    result = obj.findDuplicate3(nums)
    print(result)