from typing import List

class Solution():
    def moveZeros(self, nums: List[int]) -> List[int]:
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
        return nums

        


if __name__ == "__main__":
    nums = [0]
    obj = Solution()
    result = obj.moveZeros(nums)
    print(result)

