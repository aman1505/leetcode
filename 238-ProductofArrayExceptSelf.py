from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int])-> List[int]:
        result = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if nums[i] ==0 and nums[j]==0:
                    product*=1
                else:
                    product*= nums[j]
            if nums[i]==0:
                product = product/1
            else:
                product=product/nums[i]
            result.append(int(product))
        return result

if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    obj = Solution()
    result = obj.productExceptSelf(nums)
    print(result)