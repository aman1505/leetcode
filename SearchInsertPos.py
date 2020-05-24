import math
class Solution:
    def searchInsert(self, nums, target) -> int:
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = left+(right-left) //2
            if nums[mid] == target:
                break
            elif nums[mid]<target:
                left=mid+1
            else:
                right = mid-1

        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
            return mid
        else:
            return mid+1


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    obj = Solution()
    print(obj.searchInsert(nums,target))





