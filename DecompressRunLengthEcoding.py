from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        print(int(len(nums)/2))
        for i in range(int(len(nums)/2)):
            print(2*i)
            frequency = nums[2*i]
            value = nums[2*i+1]
            response = [value]*frequency
            result = result + response         
        return result

if __name__ == "__main__":
    nums = [1,1,2,3]
    obj = Solution()
    result = obj.decompressRLElist(nums)
    print(result)
