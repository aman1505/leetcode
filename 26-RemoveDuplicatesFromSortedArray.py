from typing import  List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int :
        # count=0
        i=0
        while (i < len(nums)-1):
            if(nums[i]==nums[i+1]):
                # del(nums[i])
                nums.remove(nums[i])
                # count+=1
            else:
                i+=1
        return len(nums),nums
            

        # for i in range(len(nums)):
        #     if (i+1 == len(nums)):
        #         break
        #     if nums[i]==nums[i+1]:
        #         nums.remove(nums[i])
        #         count = count+1
        # return count+1, nums


if __name__ == "__main__":
    nums = [1,1,2,3,4,4,5,6,6,7]
    obj = Solution()
    result = obj.removeDuplicates(nums)
    print(result)
    


#i=0 nums = [0,1,1,1,1,2,2,3,3,4]
#i=1 nums = [0,1,1,1,1,2,2,3,3,4]