from typing import List

class Solution:

    def hello(self):
        print("hello")
        return "hello"

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        print("test")
        print(nums)
        return nums


if __name__ == '__main__':
    ip = [1, 2, 3, 4, 5]
    obj = Solution()
    a = obj.hello()
    b = obj.smallerNumbersThanCurrent(ip)