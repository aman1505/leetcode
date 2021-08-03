from typing import List
class Solution:
    def findKthLargestElement(self, nums: List[int], k: int) -> int:
        result = 0 
        count = 0         

        for i in range(len(nums)):
            count+=1
            max_index = i
            for j in range(i+1,len(nums)):
                if nums[max_index] < nums[j]:
                    max_index = j
            nums[i],nums[max_index] = nums[max_index], nums[i]
            print(nums)
            if k == count:
                break
        
        result = nums[k-1]

        return result 

if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4

    obj = Solution()
    result = obj.findKthLargestElement(nums,k)
    print(result)